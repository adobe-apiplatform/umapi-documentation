# List and Query Products

Information about Adobe products used in your organization is available through the **{orgId}/products/** resource.

* Retrieve a paged list of all products for your organization:

```
GET [UM_Server]/{orgId}/products
```
* Access information for individual products by their unique ID.

```
GET [UM_Server]/{orgId}/products/{productId}
```

***

## List Products

A GET request to the **/{orgId}/products/** resource retrieves a paged list of Adobe products that your organization uses.

```json
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

***

## Query Individual Products

A GET request to the **{orgId}/products/{productId}** resource retrieves the product information for an individual Adobe product. The body of the response contains the product information in JSON format.

```json
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
