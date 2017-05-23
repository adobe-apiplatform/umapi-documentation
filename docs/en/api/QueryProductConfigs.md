---
layout: default
nav_link: Query Product Configurations
nav_order: 540
nav_level: 3
lang: en
---

# List and Query Product Configurations

Each product is associated with license configurations that are defined for your organization in the [Admin Console](https://adminconsole.adobe.com/enterprise/), and associated with an identifying nickname. Information about defined product configurations is available through individual product resources within the organization.

* Retrieve a paged list of all license configurations for the organization:

```
GET [UM_Server]/groups/{orgId}/{page}
```


See [List All Configurations for Organization](#list-all-configurations-for-organization)
* Retrieve a paged list of all product configurations for a product:

```
GET [UM_Server]/{orgId}/products/{productId}/configurations
```


See [List Configurations for Products](#list-configurations-for-products)
* Access information for individual product configurations by their identifying nickname:

```
GET [UM_Server]/{orgId}/products/{productId}/
           configurations/{configId}
```


See [Query Individual Product Configurations](#query-individual-product-configurations)
* List all members or members with admin rights in a configuration:

```
  GET [UM_Server]/{orgId}/products/{productId}/
       configurations/{configId}/users
  GET [UM_Server]/{orgId}/products/{productId}/
      configurations/{configId}/admins
```


See [List Member Users](#list-member-users)

***

## List All Configurations for Organization

A GET request to the **groups/{orgId}** resource retrieves a paged list of all product configurations that have been defined for your organization in the [Admin Console](https://adminconsole.adobe.com/enterprise/).

```json
GET [UM_Server]/groups/{orgId}/{page}
```

* **{orgId}** : Required. The unique ID of your organization.
* **{page}** : Required. A zero-based index for the start entry of a paged response.
The number of product configurations returned in each call is subject to change, but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list.

***

## List Configurations for Products

A GET request to the **configurations** resource for a specific product retrieves a paged list of Adobe product configurations defined for that product.

```json
GET [UM_Server]/{orgId}/products/{productId}/configurations[?page={n}]
```

* **{orgId}** : Required. The unique ID of your organization.
* **page={n}** : Optional. A zero-based index for the start entry of a paged response. Default is 0.
The number of products returned in each call is subject to change, but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list.

### Responses

A successful request returns a response with **HTTP status 200**. The response body contains the requested product configuration data in JSON format:

```json
{
    "id": "XXXX-123456789ABCD",
    "code": "SUPPORT",
    "name": "Support",
    "userCount": 1,
    "configurationCount": 2,
    "licenseQuota": 10,
    "licenseConfigurations": [
        {
            "id": "XXXX-8A3EA521D2BCA92C5E4B",
            "adminCount": 0,
            "userCount": 0,
            "licenseQuota": null,
            "licenseGroupId": 22277479,
            "adminGroupId": 22277482,
            "orgId": "UDI123UID123@AdobeOrg",
            "productId": "XXXX-123456789ABCD"
        },
        {
            "id": "XXXX-FC6F915670D9DEA946DB",
            "adminCount": 0,
            "userCount": 1,
            "licenseQuota": null,
            "licenseGroupId": 28809409,
            "adminGroupId": 28809412,
            "orgId": "UDI123UID123@AdobeOrg",
            "productId": "XXXX-123456789ABCD"
        }
    ]
}
```

A failed request can result in a response with one of these HTTP status values, with an error message in the response body:

* **400 Bad Request** : Some parameters of the request were not understood by the server.
* **401 Unauthorized** : Invalid or expired token.
* **403 Forbidden** : x-api-key header is missing.
* **404 Not Found** : productId or configId was not found.

_Note that server errors can occur that require exponential back-off on retry._

***

## Query Individual Product Configurations

A GET request to the **{orgId}/products/{productId}/configurations/{configId}** resource retrieves information for a defined product configuration. The body of the response contains the configuration information in JSON format.

```json
   GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}
```

* **{orgId}** : Required. Your organization ID.
* **{productId}** : Required. The unique ID of the product.
* **{configId}** : Required. The unique ID of the product configuration.

### Responses

A successful request returns the requested data with **HTTP status 200**. The response body contains the requested product data in JSON format.

```json
{
  "id": "XXXX-95D51A5143B613E484DB",
  "adminCount": 0,
  "userCount": 226,
  "licenseQuota": 0,
  "licenseGroupId": 20337301,
  "adminGroupId": 20337304,
  "orgId": "UDI123UID123@AdobeOrg",
  "productId": "XXXX-123456789ABCD"
}
```

***

## List Member Users

A GET request to the **users** or **admins** resource under a specific product  configuration returns a list of all members or members with admin rights in that configuration.

```
   GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}/users
   GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}/admins
```

```json
GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}/admins[?page={n}]
```

* **orgId** : Required. The unique ID of your organization.
* **page** : Optional zero-based index for the start entry of the paged response. Default is 0.
The number of users returned in each call is subject to change, but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list.


### Responses

A successful request returns a response with **HTTP status 200**. The response body contains the requested user data in JSON format:

```
{
  "result": "success",
  "users" : [ { user1 }, ... ]
  "lastPage" : true
}
```

A failed request can result in a response with one of these HTTP status values, with an error message in the response body:

* **400 Bad Request** : Some parameters of the request were not understood by the server.
* **401 Unauthorized** : Invalid or expired token.

_Note that server errors can occur that require exponential back-off on retry._
