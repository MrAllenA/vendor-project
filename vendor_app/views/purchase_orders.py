import uuid
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from vendor_app.models import CustomUser,Vendor,PurchaseOrder
from ..serializers.vendor_serializer import VendorSerializer
from ..serializers.purchase_order_serializer import PurchaseOrderSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from django.shortcuts import get_object_or_404
from django.db import models


@api_view(['POST','GET'])
@authentication_classes([])
@permission_classes([])
def purchase_order_create(request,pk=None):
    if request.method =='POST':
        data = request.data
        custom_po_number = f"po{uuid.uuid4()}"
        data["po_number"] = custom_po_number
        # Set the vendor based on the logic you've used before
        vendor = Vendor.objects.annotate(num_orders=models.Count('purchaseorders')).order_by('num_orders').first()
        data['vendor'] = vendor.id  
        serializer = PurchaseOrderSerializer(data=data)
        if serializer.is_valid():
            # Save the data to create a new PurchaseOrder instance
            purchase_order_instance = serializer.save()

            # Return the serialized data with a 201 status code
            serialized_data = PurchaseOrderSerializer(purchase_order_instance).data

    if request.method == "GET":
        if pk:
            vendor = get_object_or_404(Vendor, id=pk)
            orders = PurchaseOrder.objects.filter(vendor=vendor)
            serializer= PurchaseOrderSerializer(orders,many=True)
        else:
            orders = PurchaseOrder.objects.all()
            serializer = PurchaseOrderSerializer(orders,many=True)
        return Response(serializer.data,status=200)



    
