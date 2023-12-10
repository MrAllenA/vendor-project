from django.contrib import admin
from .models import (Vendor,CustomUser,PurchaseOrder)
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display=['username']

class VendorAdmin(admin.ModelAdmin):
    list_display=['vendor_code','contact_details','address','name','on_time_delivery_rate','quality_rating_avg','average_response_time','fullfillment_rate']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Vendor,VendorAdmin)