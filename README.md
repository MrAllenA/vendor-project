# Vendor and Purchase Order Management API

This API provides functionality for managing vendors and purchase orders. It supports operations such as creating, updating, and deleting vendors, as well as creating, updating, and acknowledging purchase orders.

## Table of Contents

- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [1. Create Vendor (POST /vendors/)](#1-create-vendor-post-vendors)
  - [2. List Vendors (GET /vendors/)](#2-list-vendors-get-vendors)
  - [3. Update Vendor (PUT /vendors/)](#3-update-vendor-put-vendors)
  - [4. Delete Vendor (DELETE /vendors/)](#4-delete-vendor-delete-vendors)
  - [5. Get Vendor Details (GET /vendors/id/)](#5-get-vendor-details-get-vendorsid)
  - [6. Create Purchase Order (POST /purchase_orders/)](#6-create-purchase-order-post-purchase_orders)
  - [7. List Vendor Purchase Orders (GET /purchase_orders/id)](#7-list-vendor-purchase-orders-get-purchase_ordersid)
  - [8. List All Purchase Orders (GET /purchase_orders/)](#8-list-all-purchase-orders-get-purchase_orders)
  - [9. Get Purchase Order Details (GET /purchase_orders/id/)](#9-get-purchase-order-details-get-purchase_ordersid)
  - [10. Update Purchase Order (PUT /purchase_orders/id/)](#10-update-purchase-order-put-purchase_ordersid)
  - [11. Delete Purchase Order (DELETE /purchase_orders/id/)](#11-delete-purchase-order-delete-purchase_ordersid)
  - [12. Acknowledge Purchase Order (POST /purchase_orders/id/acknowledge)](#12-acknowledge-purchase-order-post-purchase_ordersidacknowledge)
  - [13. Get Vendor Performance Metrics (GET /vendors/id/performance)](#13-get-vendor-performance-metrics-get-vendorsidperformance)

## Authentication

- Some endpoints require authentication.
- Include the authentication token in the request headers.
- http://127.0.0.1:8000/swagger/ you will get all the endpoints
- ![alt text](https://github.com/MrAllenA/vendor-project/blob/master/swagger.png)
- You can Put token here on top left you have authorize
- ![alt text](https://github.com/MrAllenA/vendor-project/blob/master/authorize.png)
- input token like this
- ![alt text](https://github.com/MrAllenA/vendor-project/blob/master/tokenauth.png)

## Endpoints

### 1. Create Vendor (POST /vendors/) - no authentication required , POST request to this will create vendor

Create a new vendor.

**Request:**
```json
{
  "vendor": "testor1",
  "contact_details": "95352343324 road no",
  "address": "near 2nd lane road"
}

**Response:**
{
  "token": "token 0880fe6847cd56bc8aba750a270c8ebdf25aa4fb",
  "vendor_code": "ven5db0e212-3f5e-4e00-8d3f-9485b3e99035",
  "vendor_id": 21
}

