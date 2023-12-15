from collections.abc import Iterable
from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin
from django.db.models.signals import pre_save,post_save
from django.db.models import Q,F,Avg
from django.shortcuts import get_object_or_404
from datetime import timedelta

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a regular user with an email and password.
        """
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creates and saves a superuser with an username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True)
    is_staff = models.BooleanField(default=False)
    # other fields...
    USERNAME_FIELD= 'username'
    # Use the custom manager for the user model
    objects = CustomUserManager()

    # Rest of your custom user model implementation...

class Vendor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,blank=True,related_name='vendor_user')
    vendor_code = models.CharField(null=False,blank=True,unique=True)
    name = models.CharField(max_length=255,null=False,blank=True)
    contact_details = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    on_time_delivery_rate = models.FloatField(null=True,blank=True,default=0.0)
    quality_rating_avg = models.FloatField(null=True,blank=True,default=0.0)
    average_response_time = models.FloatField(null=True,blank=True,default=0.0)
    fullfillment_rate = models.FloatField(null=True,blank=True,default=0.0)

    def __str__(self) -> str:
        return self.vendor_code
    
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50,null=False,blank=True, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,related_name="purchaseorders",null=True,blank=True)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField(null=True,blank=True)
    items = models.JSONField(null=False,blank=True)
    quantity = models.IntegerField(null=False,blank=True)
    status = models.CharField(max_length=50,default="pending",null=False,blank=True)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(null=True,blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Purchase Order {self.po_number}"
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True,blank=True)
    on_time_delivery_rate = models.FloatField(null=True,blank=True,default=0.0)
    quality_rating_avg = models.FloatField(null=True,blank=True,default=0.0)
    average_response_time = models.FloatField(null=True,blank=True,default=0.0)
    fullfillment_rate = models.FloatField(null=True,blank=True,default=0.0)

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
    

def create_historical_performance(sender,instance,**kwargs):
        if instance.status == "completed":
            vendor = instance.vendor
            HistoricalPerformance.objects.create(vendor=vendor,date=timezone.localtime(timezone.now()),on_time_delivery_rate=vendor.on_time_delivery_rate,quality_rating_avg=vendor.quality_rating_avg,average_response_time=vendor.average_response_time,fullfillment_rate=vendor.fullfillment_rate)

            orders_completed = PurchaseOrder.objects.filter(vendor=vendor,status="completed",delivery_date__gte=F('acknowledgment_date'))
            total_orders_completed = PurchaseOrder.objects.filter(vendor=vendor,status="completed")
            print(orders_completed,total_orders_completed)
            on_time_delivery_rate = orders_completed.count() / total_orders_completed.count() if total_orders_completed.count() > 0 else 0.0
            vendor.on_time_delivery_rate = on_time_delivery_rate
            
            completed_orders_with_quality_rating = PurchaseOrder.objects.filter(vendor=vendor,status="completed",quality_rating__isnull=False)
            quality_rating_average = completed_orders_with_quality_rating.aggregate(Avg('quality_rating'))['quality_rating__avg']
            vendor.quality_rating_avg =quality_rating_average

            acknowledged_orders_for_vendor = PurchaseOrder.objects.filter(vendor=vendor,acknowledgment_date__isnull=False)
            time_diffs = [(po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_orders_for_vendor]
            for po in acknowledged_orders_for_vendor:
                print(f"Acknowledgment Date: {po.acknowledgment_date}, Issue Date: {po.issue_date}")
            average_response_time = sum(time_diffs) / len(time_diffs) if time_diffs else 0.0
            vendor.average_response_time =average_response_time

            fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor,status="completed")
            total_orders_issued = PurchaseOrder.objects.filter(vendor=vendor)
            fulfillment_rate = fulfilled_orders.count() / total_orders_issued.count() if total_orders_issued else 0.0
            vendor.fullfillment_rate = fulfillment_rate
            vendor.save()
        




post_save.connect(create_historical_performance,sender=PurchaseOrder)