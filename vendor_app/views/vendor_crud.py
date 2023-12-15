import uuid
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from vendor_app.models import CustomUser,Vendor,HistoricalPerformance
from ..serializers.vendor_serializer import VendorSerializer,MetricsSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(method='POST',request_body=openapi.Schema(type=openapi.TYPE_OBJECT,properties={'vendor':openapi.Schema(type=openapi.TYPE_STRING),'contact_details':openapi.Schema(type=openapi.TYPE_STRING),'address':openapi.Schema(type=openapi.TYPE_STRING),},required=['vendor']),  consumes=['application/json'],)
@api_view(['POST','GET'])
@authentication_classes([])
@permission_classes([])
def vendor_create(request,pk=None):
    if request.method =='POST':
        username = request.data.get('vendor', None)
        contact_details = request.data.get('contact_details', None)
        address = request.data.get('address', None)
        if not username:
            return Response("No vendor name given",status=406)
        try:
            #check if vendor already exist
            vendor_check = CustomUser.objects.filter(username=username)
            if not vendor_check:

                uuidvendor = "ven" + str(uuid.uuid4())

                vendor = CustomUser.objects.create(username=username)
                vendor_confirm = Vendor.objects.create(user=vendor,name=username,contact_details=contact_details,address=address,vendor_code=uuidvendor)
                if vendor_confirm:
                    user = Token.objects.create(user=vendor)
                    token = user.key
                    content ={
                        "token": token,
                        "vendor_code": vendor_confirm.vendor_code,
                        "vendor id": vendor_confirm.id
                    }
                    return Response(content,status=201)
            else:
                return Response("username already exists",status=406)

        except Exception as e:
            print(e)
            return Response(status=400)
    
    if request.method == "GET":
        return vendor_list_and_update(request._request,pk)
    

@swagger_auto_schema(method='PUT',request_body=openapi.Schema(type=openapi.TYPE_OBJECT,properties={'name':openapi.Schema(type=openapi.TYPE_STRING),'contact_details':openapi.Schema(type=openapi.TYPE_STRING),'address':openapi.Schema(type=openapi.TYPE_STRING)}),  consumes=['application/json'],)
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def vendor_list_and_update(request,pk):
    if request.method == 'GET':
        if pk:
                vendors= get_object_or_404(Vendor,id=pk)
                serializer = VendorSerializer(vendors)
        else:
            vendors= Vendor.objects.all()
            serializer = VendorSerializer(vendors,many=True)
        response_data = serializer.data
        return Response(response_data,status=200)

    if request.method == 'PUT':
        vendor = get_object_or_404(Vendor, id=pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        vendor = get_object_or_404(Vendor, id=pk)
        user = vendor.user
        user.delete()
        return Response("Vendor deleted successfully", status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vendor_metrics(request,pk):
    if pk:
        vendor = get_object_or_404(Vendor,id=pk)
        serializer = VendorSerializer(vendor)
        metric_vendor = HistoricalPerformance.objects.filter(vendor=vendor).order_by('date')
        mertics = MetricsSerializer(metric_vendor,many=True)
        content ={
            "current_metrics":serializer.data,
            "historical metrics": mertics.data

        }
        return Response(content,status=200)
    else:
        return Response("no data found",status=400)
