from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['POST'])
def vendor_create(request):
    username = request.POST.get('vendor',None)
    if not username:
        return Response("No vendor name given",status=406)
    return Response(username,status=200)