import uuid
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from vendor_app.models import CustomUser,Vendor,PurchaseOrder
from ..serializers.vendor_serializer import VendorSerializer
from ..serializers.purchase_order_serializer import PurchaseOrderSerializer, PurchaseOrderUpdateSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from django.shortcuts import get_object_or_404
from django.db import models
from datetime import datetime
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#create purchase order
@swagger_auto_schema(method='POST',request_body=openapi.Schema(type=openapi.TYPE_OBJECT,properties={'delivery_date':openapi.Schema(type=openapi.TYPE_STRING),'items':openapi.Schema(type=openapi.TYPE_ARRAY,items=openapi.Schema(type=openapi.TYPE_OBJECT)),'quantity':openapi.Schema(type=openapi.TYPE_INTEGER),'quality_rating':openapi.Schema(type=openapi.TYPE_INTEGER)}),  consumes=['application/json'],)
@api_view(['POST','GET'])
@permission_classes([])
def purchase_order_create(request,pk=None):
    if request.method =='POST':
        data = request.data
        custom_po_number = f"po{uuid.uuid4()}"
        data["po_number"] = custom_po_number
        # Set the vendor based on the logic you've used before
        vendor = Vendor.objects.annotate(num_orders=models.Count('purchaseorders')).order_by('num_orders').first()
        if vendor:
            data['vendor'] = vendor.id 
        else:
            return Response("no vendors",status=404)

        data['issue_date'] =  timezone.localtime(timezone.now())

        delivery_date_str = data.get('delivery_date')  # Assuming 'delivery_date' is the field name
        delivery_date = datetime.strptime(delivery_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')

        if delivery_date <= datetime.today():
            return Response({"error": "Delivery date must be equal to or greater than today."}, status=400)
        
        serializer = PurchaseOrderSerializer(data=data)
        if serializer.is_valid():
            # Save the data to create a new PurchaseOrder instance
            purchase_order_instance = serializer.save()

            # Return the serialized data with a 201 status code
            serialized_data = PurchaseOrderSerializer(purchase_order_instance).data

            return Response(serialized_data,status=201)
# get all orders if pk is not provided or get orders of specific vendor
    if request.method == "GET":
        if pk:
            vendor = get_object_or_404(Vendor, id=pk)
            orders = PurchaseOrder.objects.filter(vendor=vendor)
            serializer= PurchaseOrderSerializer(orders,many=True)
        else:
            orders = PurchaseOrder.objects.all()
            serializer = PurchaseOrderSerializer(orders,many=True)
        return Response(serializer.data,status=200) 

#get,update,delete specific order for id
@swagger_auto_schema(method='PUT',request_body=openapi.Schema(type=openapi.TYPE_OBJECT,properties={'delivery_date':openapi.Schema(type=openapi.TYPE_STRING),'items':openapi.Schema(type=openapi.TYPE_ARRAY,items=openapi.Schema(type=openapi.TYPE_OBJECT)),'quantity':openapi.Schema(type=openapi.TYPE_INTEGER),'quality_rating':openapi.Schema(type=openapi.TYPE_INTEGER)}),  consumes=['application/json'],)
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def purchase_order_details(request,pk):
    if request.method == 'GET':
        order = get_object_or_404(PurchaseOrder,id=pk)
        serializer= PurchaseOrderSerializer(order)
        return Response(serializer.data,status=200)


    if request.method == 'PUT':
        order = get_object_or_404(PurchaseOrder, id=pk)
        serializer = PurchaseOrderUpdateSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        order = get_object_or_404(PurchaseOrder, id=pk)
        order.delete()
        return Response("Purchase Order deleted successfully", status=200)

#acknowledge order
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def purchase_order_acknoweldgement(request,pk):
    user_instance = request.user
    vendor = get_object_or_404(Vendor,user=user_instance)
    order = get_object_or_404(PurchaseOrder,id=pk,vendor=vendor)
    if not order:
        return Response("Purchase order doesnt exist",status=404)
    if order.status == "completed":
        return Response("already completed",status=200)
    order.acknowledgment_date = timezone.localtime(timezone.now())
    order.status = "completed"
    order.save()
    serializer = PurchaseOrderSerializer(order)
    return Response(serializer.data,status=201)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def purchase_order_completed(request,pk):
#     user_instance = request.user
#     vendor = get_object_or_404(Vendor,user=user_instance)
#     order = get_object_or_404(PurchaseOrder,id=pk,vendor=vendor)
#     if not order:
#         return Response("Purchase order doesnt exist",status=404)
#     if order.status == "completed":
#         return Response("already completed",status=200)
#     else:
#         order.save()
#     serializer = PurchaseOrderSerializer(order)
#     return Response(serializer.data,status=201)