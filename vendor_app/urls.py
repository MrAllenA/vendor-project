from django.urls import path
from vendor_app.views import vendor_crud,purchase_orders

urlpatterns =[


    path('vendors/', vendor_crud.vendor_create, name='vendor-create'),
    path('vendors/<int:pk>/', vendor_crud.vendor_list_and_update, name='vendor-list'),
    path('purchase_orders/', purchase_orders.purchase_order_create, name='purchase-order-create'),
    path('purchase_orders/<int:pk>/', purchase_orders.purchase_order_create, name='purchase-order-create-vendor-filter'),
    
]