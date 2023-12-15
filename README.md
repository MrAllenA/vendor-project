# Vendor and Purchase Order Management API

This API provides functionality for managing vendors and purchase orders. It supports operations such as creating, updating, and deleting vendors, as well as creating, updating, and acknowledging purchase orders.

## Table of Contents

- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [1. Create Vendor (POST api/vendors/)](#1.-Create-Vendor-(POST-api/vendors/))
  - [2. List Vendors (GET api/vendors/)](#2-list-vendors-get-vendors)
  - [3. Retrieve Details of Specific Vendor(GET api/vendors/id/)](#3-Retrieve-vendor-details)
  - [4. Update Vendor (PUT api/vendors/id/)](#3-update-vendor-put-vendors)
  - [5. Delete Vendor (DELETE api/vendors/id/)](#4-delete-vendor-delete-vendors)
  - [6. Create Purchase Order (POST api/purchase_orders/)](#6-create-purchase-order-post-purchase_orders)
  - [7. List All Purchase Orders (GET api/purchase_orders/)](#8-list-all-purchase-orders-get-purchase_orders)
  - [8. List Vendor Purchase Orders (GET api/purchase_orders/id)](#7-list-vendor-purchase-orders-get-purchase_ordersid)
  - [9. Get Purchase Order Details (GET api/purchase_orders/id/)](#9-get-purchase-order-details-get-purchase_ordersid)
  - [10. Update Purchase Order (PUT api/purchase_orders/id/)](#10-update-purchase-order-put-purchase_ordersid)
  - [11. Delete Purchase Order (DELETE api/purchase_orders/id/)](#11-delete-purchase-order-delete-purchase_ordersid)
  - [12. Acknowledge Purchase Order (POST api/purchase_orders/id/acknowledge)](#12-acknowledge-purchase-order-post-purchase_ordersidacknowledge)
  - [13. Get Vendor Performance Metrics (GET api/vendors/id/performance)](#13-get-vendor-performance-metrics-get-vendorsidperformance)

## Authentication

- Some endpoints require authentication.
- Include the authentication token in the request headers.
- http://127.0.0.1:8000/swagger/ you will get all the endpoints
- Test All endpoints by clicking "Try Out"
- ![alt text](https://github.com/MrAllenA/vendor-project/blob/master/swagger.png)
- You can Put token here on top left you have authorize, you will get the token after creating a vendor
- ![alt text](https://github.com/MrAllenA/vendor-project/blob/master/authorize.png)
- input token like this
- ![alt text](https://github.com/MrAllenA/vendor-project/blob/master/tokenauth.png)

## Endpoints

### 1. Create Vendor (POST api/vendors/) - Authentication not required , POST request to this will create vendor

Create a new vendor.

**Request:**
```json
{
  "vendor": "testor1",
  "contact_details": "95352343324 road no",
  "address": "near 2nd lane road"
}
```
**Response:**
```json
{
  "token": "token 0880fe6847cd56bc8aba750a270c8ebdf25aa4fb",
  "vendor_code": "ven5db0e212-3f5e-4e00-8d3f-9485b3e99035",
  "vendor_id": 21
}
```
> [!NOTE]
> Add token keyword before token like this - token 0880fe6847cd56bc8aba750a270c8ebdf25aa4fb

### 2. List Vendors (GET api/vendors/) - Authentication required , POST request to this will return list of all vendors

Response
```json
[
  {
    "id": 21,
    "vendor_code": "ven5db0e212-3f5e-4e00-8d3f-9485b3e99035",
    "name": "testor1",
    "contact_details": "95352343324 road no ",
    "address": "near 2nd lane road",
    "on_time_delivery_rate": 0,
    "quality_rating_avg": 0,
    "average_response_time": 0,
    "fullfillment_rate": 0,
    "user": 22
  }
]
```
> [!NOTE]
> The id here and the vendor id got when you created the vendor is same, so please note the vendor id.


### 3. Retrieve Details of Specific Vendor (GET api/vendors/id/) - Authentication required , GET request to this will return list of all vendors

| parameter  | value |
| ------------- | ------------- |
|  id  | vendors id(eg. 21)  |

Response
```json
[
  {
    "id": 21,
    "vendor_code": "ven5db0e212-3f5e-4e00-8d3f-9485b3e99035",
    "name": "testor1",
    "contact_details": "95352343324 road no ",
    "address": "near 2nd lane road",
    "on_time_delivery_rate": 0,
    "quality_rating_avg": 0,
    "average_response_time": 0,
    "fullfillment_rate": 0,
    "user": 22
  },
  {
    "id": 22,
    "vendor_code": "ven7dbg0e232-325e-4100-8d3s-94d5bde9d035",
    "name": "testor1",
    "contact_details": "95352343324 road no ",
    "address": "near 2nd lane road",
    "on_time_delivery_rate": 0,
    "quality_rating_avg": 0,
    "average_response_time": 0,
    "fullfillment_rate": 0,
    "user": 22
  }
]
```
### 4.  Update Vendor (PUT api/vendors/id/) - Authentication required , PUT request to this will update vendor details for the vendor id you have provided

| parameter  | value |
| ------------- | ------------- |
|  id  | vendors id(eg. 21)  |

**Request**
```json
{
  "name": "tester",
  "contact_details": "new contact",
  "address": "new address"
}
```


**Response**
```json
{
  "id": 21,
  "vendor_code": "ven5db0e212-3f5e-4e00-8d3f-9485b3e99035",
  "name": "tester",
  "contact_details": "new contact",
  "address": "new address",
  "on_time_delivery_rate": 0,
  "quality_rating_avg": 0,
  "average_response_time": 0,
  "fullfillment_rate": 0,
  "user": 22
}
```
> [!NOTE]
> id : 21 - or the id of the vendor you want to update

### 5.  Delete Vendor (DELETE api/vendors/id/) - Authentication required , DELETE request to this will delete vendor for the id you have provided

| parameter  | value |
| ------------- | ------------- |
|  id  | vendors id(eg. 21)  |

**Response**
```json
{"Vendor deleted successfully"}
```

### 6. Create Purchase Order (POST api/purchase_orders/) - Authentication not required , POST to this will create purchase order, this purchase order will be assigned to the vendor with the least orders

**Request**
```json
{
  "delivery_date": "2023-12-31T15:20:16.481960Z",
  "items": [{"item_name": "item1"}, {"item_name": "item2"}],
  "quantity": 15,
   "quality_Rating":3
}
```
**Response**
```json
{
  "id": 34,
  "po_number": "poa4fe783c-551c-48db-8876-381590063bd7",
  "order_date": "2023-12-15T22:15:15.423349+05:30",
  "delivery_date": "2023-12-31T20:50:16.481960+05:30",
  "items": [
    {
      "item_name": "item1"
    },
    {
      "item_name": "item2"
    }
  ],
  "quantity": 15,
  "status": "pending",
  "quality_rating": null,
  "issue_date": "2023-12-15T22:15:15.408343+05:30",
  "acknowledgment_date": null,
  "vendor": 21
}
```
> [!NOTE]
> id : purchase order id is 34

### 7. List All Purchase Orders (GET api/purchase_orders/) - Authentication not required , GET to this will list all the purchase orders

**Response**
```json
[
  {
    "id": 34,
    "po_number": "poa4fe783c-551c-48db-8876-381590063bd7",
    "order_date": "2023-12-15T22:15:15.423349+05:30",
    "delivery_date": "2023-12-31T20:50:16.481960+05:30",
    "items": [
      {
        "item_name": "item1"
      },
      {
        "item_name": "item2"
      }
    ],
    "quantity": 15,
    "status": "pending",
    "quality_rating": null,
    "issue_date": "2023-12-15T22:15:15.408343+05:30",
    "acknowledgment_date": null,
    "vendor": 21
  },
    "id": 35,
    "po_number": "poadfe783c-f51c-48d4-7674-dsg81590gs63bd7",
    "order_date": "2023-12-15T22:15:15.423349+05:30",
    "delivery_date": "2023-12-17T20:50:16.481960+05:30",
    "items": [
      {
        "item_name": "item1"
      },
      {
        "item_name": "item2"
      }
    ],
    "quantity": 15,
    "status": "pending",
    "quality_rating": null,
    "issue_date": "2023-12-15T22:15:15.408343+05:30",
    "acknowledgment_date": null,
    "vendor": 22
  }

]
```
### 8. List Vendor Purchase Orders (GET api/purchase_orders/id) - Authentication not required , GET to this will list all the purchase orders of the vendor for the id given 

| parameter  | value |
| ------------- | ------------- |
|  id  | vendors id(eg. 21)  |

**Response**
```json
[
  {
    "id": 34,
    "po_number": "poa4fe783c-551c-48db-8876-381590063bd7",
    "order_date": "2023-12-15T22:15:15.423349+05:30",
    "delivery_date": "2023-12-31T20:50:16.481960+05:30",
    "items": [
      {
        "item_name": "item1"
      },
      {
        "item_name": "item2"
      }
    ],
    "quantity": 15,
    "status": "pending",
    "quality_rating": null,
    "issue_date": "2023-12-15T22:15:15.408343+05:30",
    "acknowledgment_date": null,
    "vendor": 21
  }
]
```

### 9. Get Purchase Order Details (GET /purchase_orders/id/) - Authentication required , GET to this will retrieve details of specific purchase order for id given

| parameter  | value |
| ------------- | ------------- |
|  id  | purchase order id (eg. 34) |


**Response**
```json
{
  "id": 34,
  "po_number": "poa4fe783c-551c-48db-8876-381590063bd7",
  "order_date": "2023-12-15T22:15:15.423349+05:30",
  "delivery_date": "2023-12-31T20:50:16.481960+05:30",
  "items": [
    {
      "item_name": "item1"
    },
    {
      "item_name": "item2"
    }
  ],
  "quantity": 15,
  "status": "pending",
  "quality_rating": null,
  "issue_date": "2023-12-15T22:15:15.408343+05:30",
  "acknowledgment_date": null,
  "vendor": 21
}

```

### 10. Update Purchase Order (PUT api/purchase_orders/id/) - Authentication required , PUT to this will update details of the purchase order for id you given

| parameter  | value |
| ------------- | ------------- |
|  id  | purchase order id (eg. 34) |

**Request**
```json

{
  "delivery_date": "2023-12-31T15:20:16.481960Z",
  "items": [{"item_name": "item1"}, {"item_name": "item2"},{"item_name": "item3"}],
  "quantity": 15,
   "quality_Rating":3
}
```

**Response**
```json
{
  "id": 34,
  "po_number": "poa4fe783c-551c-48db-8876-381590063bd7",
  "order_date": "2023-12-15T22:15:15.423349+05:30",
  "delivery_date": "2023-12-31T20:50:16.481960+05:30",
  "items": [
    {
      "item_name": "item1"
    },
    {
      "item_name": "item2"
    },
    {
      "item_name": "item3"
    }
  ],
  "quantity": 15,
  "status": "pending",
  "quality_rating": null,
  "issue_date": "2023-12-15T22:15:15.408343+05:30",
  "acknowledgment_date": null,
  "vendor": 21
}

```

### 11. Delete Purchase Order (DELETE api/purchase_orders/id/) - Authentication required , DELETE will delete the purchase order of specific purchase order for the id given

| parameter  | value |
| ------------- | ------------- |
|  id  | purchase order id (eg. 34) |


**Response**
```json
{"Purchase Order deleted successfully"}
```

### 12. Acknowledge Purchase Order (POST api/purchase_orders/id/acknowledge) - Authentication required, POST to this will acknowledge and change status of the purchase order to completed , that is the purchase order id, you have provided and this will only be changed to completed if the purchase order is assigned to the vendor your logged in as, and metrics will be calculated.

| parameter  | value |
| ------------- | ------------- |
|  id  | purchase order id (eg. 34) |


**Response**

{
  "id": 34,
  "po_number": "poa4fe783c-551c-48db-8876-381590063bd7",
  "order_date": "2023-12-15T22:42:08.457905+05:30",
  "delivery_date": "2023-12-31T20:50:16.481960+05:30",
  "items": [
    {
      "item_name": "item1"
    },
    {
      "item_name": "item2"
    },
    {
      "item_name": "item2"
    }
  ],
  "quantity": 15,
  "status": "completed",
  "quality_rating": null,
  "issue_date": "2023-12-15T22:15:15.408343+05:30",
  "acknowledgment_date": "2023-12-15T22:42:08.457905+05:30",
  "vendor": 21
}

> [!NOTE]
> An already acknowledged PO cant be acknowledged again

### 13. Get Vendor Performance Metrics (GET api/vendors/id/performance) - authentication required, GET request will fetch the current metrics of vendor and all the historical metrics

| parameter  | value |
| ------------- | ------------- |
|  id  | vendors id(eg. 21)  |

**Response**
```json
{
  "current_metrics": {
    "id": 21,
    "vendor_code": "ven5db0e212-3f5e-4e00-8d3f-9485b3e99035",
    "name": "tester",
    "contact_details": "new contact",
    "address": "new address",
    "on_time_delivery_rate": 1,
    "quality_rating_avg": null,
    "average_response_time": 1613.049562,
    "fullfillment_rate": 1,
    "user": 22
  },
  "historical metrics": [
    {
      "id": 18,
      "date": "2023-12-15T22:42:08.457905+05:30",
      "on_time_delivery_rate": 0,
      "quality_rating_avg": 0,
      "average_response_time": 0,
      "fullfillment_rate": 0,
      "vendor": 21
    }
  ]
}
```







