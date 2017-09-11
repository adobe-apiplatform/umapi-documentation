---
title: Get Product Profile
layout: default
nav_link: Get Product Profile
nav_order: 451
nav_level: 3
lang: en
---
# Get Product Profile

```
GET /v2/usermanagement/{orgId}/products/{productId}/configurations/{configId}
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#throttle)

<a name="intro" class="api-ref-subtitle"></a>
This API retrieves details of a single product profile withing a specified organization by searching for product id and configuration id. Successful queries will return a 200 response whose body is a single JSON response representing the product profile information. 

__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#throttle) for full details.

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

This table summarizes the parameters and how they are provided:

| Name | Type | Required | Description |
| :---- | :------ | :---: | :------ |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| productId | path | true | {% include apiRef/productIdDescription.md %} |
| licenseId | path | true | {% include apiRef/licenseIdDescription.md %} |
| x-api-key | header | true | {% include apiRef/apiKeyDescription.md %} |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| Content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
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

#### Schema Properties

- __id:__ _string_
- __adminCount:__ _long_; {% include apiRef/adminCountDescription.md %}  
- __userCount:__ _long_; {% include apiRef/userCountDescription.md %}  
- __licenseQuota:__ _Integer_; {% include apiRef/licenseQuotaDescription.md %}  
- __licenseGroupId:__ _Long_; {% include apiRef/licenseIdDescription.md %}  
- __adminGroupId:__ _Long_; {% include apiRef/adminGroupIdDescription.md %}  
- __orgId:__ _string_; {% include apiRef/orgIdDescription.md %}  
- __productId:__ _string_; {% include apiRef/productIdDescription.md %}  

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

{% include apiRef/badRequest.md anchor="400getPLC" %}

{% include apiRef/unauthorized.md anchor="401getPLC" %}

{% include apiRef/forbidden.md anchor="403getPLC" %}

{% include apiRef/notFound.md object="plc" anchor="404getPLC" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
```
curl -X GET https://usermanagement-stage.adobe.io/v2/usermanagement/12345@AdobeOrg/products/RPC-VTT1HB5NYDEBQMT5K30NQPNKTW/configurations/RGRP-13570983 \
 --header 'authorization: Bearer ey...' \
 --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```

## <a name="throttle" class="api-ref-subtitle">Throttling</a>

{% include apiRef/throttling.md client=5 global=100 %}