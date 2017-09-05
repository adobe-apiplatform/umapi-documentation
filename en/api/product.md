---
title: Access Product Information
layout: default
nav_link: Access Product Information
nav_order: 450
nav_level: 2
lang: en
---

# Products

The following set of APIs allow users to retrieve information about their organization's [products](glossary.html#product).

_Product_ access for individual users is controlled through membership in [user-groups](glossary.html#usergroup) and [product configurations](glossary.html#plc). You cannot create these groups through the User Management API. Before you can manage product access for users, you must create and name user groups and product configurations using the [Admin Console](glossary.html#adminconsole).

A product can have more than one license configuration associated with it, to allow different access privileges for different sets of users. For example, if your organization uses Adobe Document Cloud Pro, you could have one product configuration that blocks access to related services and another that only allows access to E-sign services.

Both individual users and user groups can be members of a product configuration. An individual user can gain access to a particular product directly, or through user-group membership. Within a product configuration, member users can be assigned an admin role.

You can manage access for individual users through the [Action API](ActionsRef.html) endpoint or manage access rights through the individual endpoints for products and product configurations that are listed below.

* [Get a product configuration](#getProductConfiguration)
* [Get a list of users in a product configuration](#getProductConfigurationUsers)

<hr class="api-ref-rule">

GET /v2/usermanagement/{orgId}/products/{productId}/configurations/{configId}

This API retrieves details of a single product configuration withing a specified organization by searching for product id and configuration id. Successful queries will return a 200 response whose body is a single JSON response representing the product configuration information. 

### __Example Requests__
```
curl -X GET https://usermanagement-stage.adobe.io/v2/usermanagement/12345@AdobeOrg/products/RPC-VTT1HB5NYDEBQMT5K30NQPNKTW/configurations/RGRP-13570983 \
 --header 'authorization: Bearer ey...' \
 --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```

## __Parameters__

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Data Type | Req? |
| :---- | :------ | :--- | :--- | ---: |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| productId | {% include apiRef/productIdDescription.md %} | path | string | true |
| licenseId | {% include apiRef/licenseIdDescription.md %} | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
{:.bordertablestyle}

## Throttling

{% include apiRef/throttling.md client=5 global=100 %}

## __Responses__

__Content-Type:__ _application/json_

### __200 OK__
The response body contains the requested product configuration data in JSON format. Fields can be missing if values were never supplied or are not applicable for a particular product configuration.

#### __Examples__

```json
{
    "id": "RGRP-42201538",
    "adminCount": 0,
    "userCount": 2,
    "licenseQuota": 0,
    "licenseGroupId": 42201538,
    "adminGroupId": 42201541,
    "orgId": "28E1E2EB570F90057F000101@AdobeOrg",
    "productId": "RPC-09F12CBA72AA7B965D0D"
}
```

#### __Schema Properties__

- __id:__ _string_
- __adminCount:__ _long_; {% include apiRef/adminCountDescription.md %}  
- __userCount:__ _long_; {% include apiRef/userCountDescription.md %}  
- __licenseQuota:__ _Integer_; {% include apiRef/licenseQuotaDescription.md %}  
- __licenseGroupId:__ _Long_; {% include apiRef/licenseIdDescription.md %}  
- __adminGroupId:__ _Long_; {% include apiRef/adminGroupIdDescription.md %}  
- __orgId:__ _string_; {% include apiRef/orgIdDescription.md %}  
- __productId:__ _string_; {% include apiRef/productIdDescription.md %}  

#### __Schema Model__

```json
{
    "id": "string",
    "adminCount": Long,
    "userCount": Long,
    "licenseQuota": Integer,
    "licenseGroupId": Long,
    "adminGroupId": Long,
    "orgId": "string",
    "productId": "string"
}
```

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}

{% include apiRef/notFound.md object="plc" %}

<hr class="api-ref-rule">

GET /v2/usermanagement/{orgId}/products/{productId}/configurations/{configId}/users

This API retrieves a list of users, including information about them, who are associated with the specified product configuration. Fields can be missing if values were never supplied.

### __Example Requests__
```
curl -X GET https://usermanagement-stage.adobe.io/v2/usermanagement/12345@AdobeOrg/products/RPC-VTT1HB5NYDEBQMT5K30NQPNKTW/configurations/RGRP-13570983/users \
 --header 'authorization: Bearer ey...' \
 --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```

## __Parameters__

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Data Type | Req? |
| :---- | :------ | :--- | :--- | ---: |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| productId | {% include apiRef/productIdDescription.md %} | path | string | true |
| licenseId | {% include apiRef/licenseIdDescription.md %} | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
{:.bordertablestyle}

## Throttling

{% include apiRef/throttling.md client=25 global=100 %}

## __Responses__

__Content-Type:__ _application/json_

### __200 OK__
The response body contains a list of users for the product configuration in JSON format. Fields can be missing if values were never supplied or are not applicable for a particular account type.

#### __Examples__
Response returning three different user types associated with the product configuration. Possible user types returned are [adobeID](glossary.html#adobeId), [enterpriseID](glossary.html#enterpriseId), [FederatedID](glossary.html#federatedId) and [unknown](glossary.html#unknownUserType). 

```json
[
    {
        "id": "6237573D58A4C1B90A494038@example1.com",
        "email": "jane@example1.com",
        "username": "jane@example.com",
        "domain": "example.com",
        "firstName": "Jane",
        "lastName": "Doe",
        "userType": "enterpriseID"
    },
    {
        "id": "F4146FD359662BE90A49410C@AdobeID",
        "email": "johndoe@example2.com",
        "username": "johndoe@example2.com",
        "domain": "example2.com",
        "firstName": "John",
        "lastName": "Doe",
        "userType": "adobeID"
    },
    {
        "id": "4EB5B571575A6B057F000101@example.com",
        "email": "john@example.com",
        "username": "john",
        "domain": "example.com",
        "userType": "federatedId"
    },
]
```

Response returning no users associated with the product configuration.

```
[]
```

#### __Schema Properties__

* __id:__ _string_
* __email:__ _string_
* __firstName:_ _string_
* __lastName:__ _string_
* __domain:__ _string_; The user's domain.
* __userType:__ _string_; possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.html#identity) for more information.

#### __Schema Model__

```json
[ 
    {
        "id": "string",
        "email": "string",
        "firstName": "string",
        "lastName": "string",
        "domain": "string",
        "userType": "string"
    } 
]
```

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}

{% include apiRef/notFound.md object="plc" %}
