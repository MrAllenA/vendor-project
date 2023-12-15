from django.urls import path
from vendor_app.views import vendor_crud,purchase_orders

urlpatterns =[


    path('vendors/', vendor_crud.vendor_create, name='vendor-create'),
    path('vendors/<int:pk>/', vendor_crud.vendor_list_and_update, name='vendor-list'),
    path('vendors/<int:pk>/performance', vendor_crud.vendor_metrics, name='vendor-metrics'),
    path('purchase_orders/', purchase_orders.purchase_order_create, name='purchase-order-create-and-list'),
    path('purchase_orders/<int:pk>', purchase_orders.purchase_order_create, name='purchase-order-create-and-vendor-filter'),
    path('purchase_orders/<int:pk>/', purchase_orders.purchase_order_details, name='purchase-order-details-put-delete'),
    path('purchase_orders/<int:pk>/acknowledge', purchase_orders.purchase_order_acknoweldgement, name='purchase-order-acknowledge'),
    
]