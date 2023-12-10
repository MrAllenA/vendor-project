from django.urls import path
from vendor_app.views import vendor_crud

urlpatterns =[


    path('vendors/', vendor_crud.vendor_create, name='vendor-create'),
    path('vendors/<int:pk>/', vendor_crud.vendor_list_and_update, name='vendor-list')
    
]