---
layout: default
nav_link: Product APIs
nav_order: 471
nav_level: 4
lang: en
title: Product Access APIs
---
# <a name="productApis" class="api-ref-title">Product Access APIs</a>

**DEPRECATED:** These APIs have been deprecated. An exact date for removal will be confirmed before the end of 2017 but you should look to update your scripts as soon as possible.

<hr class="api-ref-rule">

Product information defined for your organization in the [Admin Console](https://adminconsole.adobe.com/enterprise/) is available through the **{orgId}/products/** resource. You can list products and examine information for individual products.

* Get a paged list of products for your organization.

```
GET /v2/usermanagement/{orgId}/products/
```
### Request headers

You must include these headers in all requests:

* **Authorization** : A current access token obtained from login request.
* **x-api-key** : The API key for your organization, obtained from the Developer Portal.

***

## List Products

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
