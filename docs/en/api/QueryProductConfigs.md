---
layout: default
nav_link: Access Product Profiles
nav_order: 452
nav_level: 3
lang: en
---

# Product Profile Query Resource Reference

You can query the Adobe database for information about product profiles that are defined for your organization. Membership in user groups and in product profiles controls a user's access to Adobe products in your organization.

* [Access Product Profile Information](#accessProductConfigurationInformation)
* [Update Product Profile Information]()

### Notation

In syntax statements for endpoints, the following notation is used:

* **[UM_Server]** is the UM API server: **https://usermanagement.adobe.io/v2/usermanagement/**
* Curly braces indicate a variable, to be replaced with specific values for your organization.
  - Replace **{orgId}** with your organization's unique ID, which looks like this: "12345@AdobeOrg".
  - Replace **{...Id}** with the unique ID assigned to the products and product profiles that are defined for you organization.
  - Replace the **{page}** element with the zero-based index for the first requested page of the paged result.

### Request headers

You must include these headers in all requests:

* **Authorization** : A current access token obtained from login request.
* **x-api-key** : The API key for your organization, obtained from the Developer Portal.

# <a name="accessProductConfigurationInformation" class="api-ref-subtitle">Access Product Profile Information</a>

Products are associated with product profiles that are defined in the [Admin Console](https://adminconsole.adobe.com/enterprise/). For a given product, you can list and examine the associated product profiles.

All products and product profiles can be accessed through endpoints under the **{orgId}/products** resource.

* List a page of product profiles defined for your organization, or for a specific product.

```
GET [UM_Server]/{orgId}/products/{productId}/configurations
```
* Retrieve information about a specific product profile.

```
GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}
```
* List a page of users who belong to a specific product profile.

```
GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}/users
```
* List a page of users with admin role for a specific product profile.

```
GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}/admins
```

## <a name="listAllConfigurationsForOrganization" class="api-ref-subtitle">List All Configurations for Organization</a>

A GET request to the **groups/{orgId}** resource retrieves a paged list of all product profiles that have been defined for your organization in the [Admin Console](https://adminconsole.adobe.com/enterprise/).

```
GET [UM_Server]/groups/{orgId}/{page}
```

* **{orgId}** : Required. The unique ID of your organization.
* **{page}** : Required. A zero-based index for the start entry of a paged response.
The number of product profiles returned in each call is subject to change, but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list.

## <a name="listConfigurationsForProducts" class="api-ref-subtitle">List Configurations for Products</a>

A GET request to the **configurations** resource for a specific product retrieves a paged list of Adobe product profiles defined for that product.

```
GET [UM_Server]/{orgId}/products/{productId}/configurations[?page={n}]
```

* **{orgId}** : Required. The unique ID of your organization.
* **page={n}** : Optional. A zero-based index for the start entry of a paged response. Default is 0.
The number of products returned in each call is subject to change, but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list.

### Responses

A successful request returns a response with **HTTP status 200**. The response body contains the requested product profile data in JSON format:

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

## <a name="queryIndividualProductConfigurations" class="api-ref-subtitle">Query Individual Product Profiles</a>

A GET request to the **{orgId}/products/{productId}/configurations/{configId}** resource retrieves information for a defined product profile. The body of the response contains the configuration information in JSON format.

```
GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}
```

* **{orgId}** : Required. Your organization ID.
* **{productId}** : Required. The unique ID of the product.
* **{configId}** : Required. The unique ID of the product profile.

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

## <a name="listMemberUsers" class="api-ref-subtitle">List Member Users</a>

A GET request to the **users** or **admins** resource under a specific product profile returns a list of all members or members with admin rights in that configuration. If you have the product profile name then you can use the alternatively [GET /v2/usermanagement/users/{orgId}/{page}/{groupName}](user.html#getUsersByGroup) API.

```
GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}/users
GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}/admins
```

```
GET [UM_Server]/{orgId}/products/{productId}/configurations/{configId}/admins[?page={n}]
```

* **orgId** : Required. The unique ID of your organization.
* **page** : Optional zero-based index for the start entry of the paged response. Default is 0.
The number of users returned in each call is subject to change, but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list.


### Responses

A successful request returns a response with **HTTP status 200**. The response body contains the requested user data in JSON format:

```json
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

## Manage Access through Product Profile Endpoints

You can manage membership and administrative rights for specific product profiles in a POST request to:
```
POST [UM_Server]/{orgId}/products/{productId}/configurations/{configId}
```

HEADERS : You must include these headers in your request:

* **Authorization** : A current access token obtained from token-exchange request.
* **Content-type** : application/json
* **x-api-key** : The API key assigned to your API client account.


The JSON payload specifies lists of users and user groups to add or remove from membership, and users for whom to add or remove the admin role. You only need to specify the lists you are modifying.
```json
{
    "addUsers": [
        "a.smith@myCompany.com"
    ],
    "removeUsers": [
        "b.jones@myCompany.com"
    ],
    "addUserGroups": [
        "UMSDK User Group"
    ],
    "removeUserGroups": [
        "UMSDK User Group 2"
    ],
    "addAdminUsers" : [
        "jdoe@myCompany.com"
    ],
    "removeAdminUsers": [
        "ann.other@myCompany.com"
    ]
}
```