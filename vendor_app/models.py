from collections.abc import Iterable
from django.db import models
from django.utils import timezone

# Create your models here.
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin

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
    on_time_delivery_rate = models.FloatField(null=True,blank=True)
    quality_rating_avg = models.FloatField(null=True,blank=True)
    average_response_time = models.FloatField(null=True,blank=True)
    fullfillment_rate = models.FloatField(null=True,blank=True)

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
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"