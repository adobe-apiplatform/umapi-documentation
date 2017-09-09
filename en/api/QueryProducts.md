---
layout: default
nav_link: Access Products
nav_order: 451
nav_level: 3
lang: en
---

# Product Query Resource Reference

You can query the Adobe database for information about products that are defined for your organization. Membership in user groups and in product profiles controls a user's access to Adobe products in your organization.

* [Access Product Information](#accessProductInformation)

### Notation

In syntax statements for endpoints, the following notation is used:

* **[UM_Server]** is the UM API server: **https://usermanagement.adobe.io/v2/usermanagement/**
* Curly braces indicate a variable, to be replaced with specific values for your organization.
  - Replace **{orgId}** with your organization's unique ID, which looks like this: "12345@AdobeOrg".
  - Replace **{productId}** with the unique ID assigned to the products defined for you organization.
  - Replace the **{page}** element with the zero-based index for the first requested page of the paged result.

### Request headers

You must include these headers in all requests:

* **Authorization** : A current access token obtained from login request.
* **x-api-key** : The API key for your organization, obtained from the Developer Portal.

***

## <a name="accessProductInformation" class="api-ref-subtitle">Access Product Information</a>

Product information defined for your organization in the [Admin Console](https://adminconsole.adobe.com/enterprise/) is available through the **{orgId}/products/** resource. You can list products and examine information for individual products.

* List a page of products for your organization.

```
GET [UM_Server]/{orgId}/products
```
* Retrieve information for a specific product.

```
GET [UM_Server]/{orgId}/products/{productId}
```

## List and Query Products

Information about Adobe products used in your organization is available through the **{orgId}/products/** resource.

* Retrieve a paged list of all products for your organization:

```
GET [UM_Server]/{orgId}/products
```
* Access information for individual products by their unique ID.

```
GET [UM_Server]/{orgId}/products/{productId}
```

### List Products

A GET request to the **/{orgId}/products/** resource retrieves a paged list of Adobe products that your organization uses.

```
GET [UM_Server]/{orgId}/products[?page={n}]
```

* **{orgId}** : Required. The unique ID of your organization.
* **page={n}** : Optional, default is 0. A zero-based index for the start entry of a paged response.

### Responses

A successful request returns a response with **HTTP status 200**. The response body contains the requested user data in JSON format:

```json
[
 {
   "id": "XXXX-ABC123456789ABCD",
   "code": "SUPPORT",
   "name": "Support",
   "userCount": 1,
   "configurationCount": 2,
   "licenseQuota": 10
  },
 {
   "id": "YYYY-DEF123456789ABCDE",
   "code": "APAP",
   "name": "Adobe Document Cloud for business",
   "userCount": 202,
   "configurationCount": 1,
   "licenseQuota": 20
  },
 {
   "id": "ZZZZ-GHI123456789ABCDE",
   "code": "CCSV",
   "name": "All Apps plan",
   "userCount": 226,
   "configurationCount": 1,
   "licenseQuota": 10
  }
]
```

A failed request can result in a response with one of these HTTP status values, with an error message in the response body:

* **400 Bad Request** : Some parameters of the request were not understood by the server.
* **401 Unauthorized** : Invalid or expired token.
* **403 Forbidden** : x-api-key header is missing.
* **404 Not Found** : productId was not found.

_Note that server errors can occur that require exponential back-off on retry._

## Query Individual Products

A GET request to the **{orgId}/products/{productId}** resource retrieves the product information for an individual Adobe product. The body of the response contains the product information in JSON format.

```
GET [UM_Server]/{orgId}/products/{productId}
```

* **{orgId}** : Required. Your organization ID.
* **{productId}** : Required. The unique ID of the product.

### Responses

A successful request returns the requested data with **HTTP status 200**. The response body contains the requested product data in JSON format.

```json
{
 [
  {
    "id": "XXXX-123456789ABCD",
    "code": "SUPPORT",
    "name": "Support",
    "userCount": 1,
    "configurationCount": 2,
    "licenseQuota": 10
   }
  ]
 }
```

## Manage Product Admin Roles
You can manage membership and administrative roles for products by sending POST requests to:

```
POST [UM_Server]/{orgId}/product/{productId}/admin
```
HEADERS : You must include these headers in your request:

* **Authorization** : A current access token obtained from token-exchange request.
* **Content-type** : application/json
* **x-api-key** : The API key assigned to your API client account.

The JSON payload specifies lists of users whom to add or remove the admin role. You only need to specify the lists you are modifying.
```json
{
    "addProductAdmin" : [
        "jdoe@myCompany.com"
    ],
    "removeProductAdmin": [
        "ann.other@myCompany.com"
    ]
}
```
