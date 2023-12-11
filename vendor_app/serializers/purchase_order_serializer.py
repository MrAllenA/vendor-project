import uuid
from rest_framework import serializers
from vendor_app.models import PurchaseOrder,Vendor
from django.db import models

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
class PurchaseOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['delivery_date','items','quantity']
