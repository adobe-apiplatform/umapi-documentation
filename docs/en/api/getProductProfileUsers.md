---
title: Get Users in Product Profile
layout: default
nav_link: Get Users in Product Profile
nav_order: 452
nav_level: 3
lang: en
---
# Get Users in Product Profile

```
GET /v2/usermanagement/{orgId}/products/{productId}/configurations/{configId}/users
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#throttle)

<a name="intro" class="api-ref-subtitle"></a>
This API retrieves a list of users, including information about them, who are associated with the specified product profile. Fields can be missing if values were never supplied.

__Throttle Limits__: Maximum 25 requests per minute per a client. See [Throttling Limits](#throttle) for full details.

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

- [200: OK](#200getPLCUsers)
- [400: Bad Request](#400getPLCUsers)
- [401: Unauthorized](#401getPLCUsers)
- [403: Forbidden](#403getPLCUsers)
- [404: Not Found](#404getPLCUsers)
- [429: Too Many Requests](#throttle)

### <a name="200getPLCUsers" class="api-ref-subtitle">200 OK</a>
The response body contains a list of users for the product profile in JSON format. Fields can be missing if values were never supplied or are not applicable for a particular account type.

#### Examples
Response returning three different user types associated with the product profile. Possible user types returned are [adobeID](glossary.html#adobeId), [enterpriseID](glossary.html#enterpriseId), [FederatedID](glossary.html#federatedId) and [unknown](glossary.html#unknownUserType). 

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

Response returning no users associated with the product profile.

```json
[]
```

#### Schema Properties

* __id:__ _string_
* __email:__ _string_
* __firstName:_ _string_
* __lastName:__ _string_
* __domain:__ _string_; The user's domain.
* __userType:__ _string_; possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.html#identity) for more information.

#### Schema Model

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

{% include apiRef/badRequest.md anchor="400getPLCUsers" %}

{% include apiRef/unauthorized.md anchor="401getPLCUsers" %}

{% include apiRef/forbidden.md anchor="403getPLCUsers" %}

{% include apiRef/notFound.md object="plc" anchor="404getPLCUsers" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
```
curl -X GET https://usermanagement-stage.adobe.io/v2/usermanagement/12345@AdobeOrg/products/RPC-VTT1HB5NYDEBQMT5K30NQPNKTW/configurations/RGRP-13570983/users \
 --header 'authorization: Bearer ey...' \
 --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```

## <a name="throttle" class="api-ref-subtitle">Throttling</a>

{% include apiRef/throttling.md client=25 global=100 %}