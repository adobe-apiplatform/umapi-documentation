---
title: Get Product Profiles for Organization
layout: default
nav_order: 472
nav_level: 4
lang: en
nav_link: Get All Profiles
---

# <a name="getAllProfiles" class="api-ref-title">Get All Product Profiles for Organization</a>

**DEPRECATED:** These APIs have been deprecated. Please use [Get User Groups and Product Profiles](group.md).

<hr class="api-ref-rule">

```
GET /v2/usermanagement/{orgId}/products/{productId}/configurations
```
This API retrieves a paged list of all product profiles that have been defined for your organization in the [Admin Console](https://adminconsole.adobe.com/enterprise/).

__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#throttle) for full details.

* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#throttle)

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

This table summarizes the parameters and how they are provided:

| Name | Type | Required | Description |
| :---- | :------ | :---: | :------ |
| orgId | path | true | {% include_relative partials/orgIdDescription.md %} |
| productId | path | true | {% include_relative partials/productIdDescription.md %} |
| licenseId | path | true | {% include_relative partials/licenseIdDescription.md %} |
| x-api-key | header | true | {% include_relative partials/apiKeyDescription.md %} |
| Authorization | header | true | {% include_relative partials/authorizationDescription.md %} |
| Content-type | header | false | {% include_relative partials/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include_relative partials/requestIdDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200getPLC)
- [400: Bad Request](#400getPLC)
- [401: Unauthorized](#401getPLC)
- [403: Forbidden](#403getPLC)
- [404: Not Found](#404getPLC)
- [429: Too Many Requests](#throttle)

### <a name="200getPLC" class="api-ref-subtitle">200 OK</a>
The response body contains the requested product profile data in JSON format. Fields can be missing if values were never supplied or are not applicable for a particular product profile.

#### Examples

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

#### Schema Properties

- __id:__ _string_
- __adminCount:__ _long_; {% include_relative partials/adminCountDescription.md %}  
- __userCount:__ _long_; {% include_relative partials/userCountDescription.md %}  
- __licenseQuota:__ _Integer_; {% include_relative partials/licenseQuotaDescription.md %}  
- __licenseGroupId:__ _Long_; {% include_relative partials/licenseIdDescription.md %}  
- __adminGroupId:__ _Long_; {% include_relative partials/adminGroupIdDescription.md %}  
- __orgId:__ _string_; {% include_relative partials/orgIdDescription.md %}  
- __productId:__ _string_; {% include_relative partials/productIdDescription.md %}  

#### Schema Model

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

{% include_relative partials/badRequest.md anchor="400getPLC" %}

{% include_relative partials/unauthorized.md anchor="401getPLC" %}

{% include_relative partials/forbidden.md anchor="403getPLC" %}

{% include_relative partials/notFound.md object="plc" anchor="404getPLC" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
```
curl -X GET https://usermanagement-stage.adobe.io/v2/usermanagement/12345@AdobeOrg/products/RPC-VTT1HB5NYDEBQMT5K30NQPNKTW/configurations/RGRP-13570983 \
 --header 'authorization: Bearer ey...' \
 --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```

## <a name="throttle" class="api-ref-subtitle">Throttling</a>

{% include_relative partials/throttling.md client=5 global=100 %}
