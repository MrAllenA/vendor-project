from django.contrib import admin
from .models import (Vendor,CustomUser,PurchaseOrder)
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display=['username']

admin.site.register(CustomUser, CustomUserAdmin)