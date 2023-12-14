from django.contrib import admin
from .models import (Vendor,CustomUser,PurchaseOrder,HistoricalPerformance)
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display=['username']

class VendorAdmin(admin.ModelAdmin):
    raw_id_fields=('user',)
    list_display=['vendor_code','contact_details','address','name','on_time_delivery_rate','quality_rating_avg','average_response_time','fullfillment_rate']

class PurchaseOrderAdmin(admin.ModelAdmin):
    raw_id_fields=('vendor',)
    list_display=['po_number','order_date','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date']


class HistoricalPerformanceAdmin(admin.ModelAdmin):
    raw_id_fields=('vendor',)
    list_display=['date','on_time_delivery_rate','quality_rating_avg','average_response_time','fullfillment_rate']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(PurchaseOrder,PurchaseOrderAdmin)
admin.site.register(HistoricalPerformance,HistoricalPerformanceAdmin)