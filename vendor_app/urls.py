from django.urls import path
from vendor_app.views import vendor_crud

urlpatterns =[


    path('vendors/', vendor_crud.vendor_create, name='vendor-create')
    
]