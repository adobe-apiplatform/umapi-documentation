---
layout: default
nav_link: Product Admin Role API
nav_order: 476
nav_level: 4
lang: en
title: Update Product Admin Roles
---
# <a name="prodAdmin" class="api-ref-title">Update Product Admin Roles</a>

**DEPRECATED:** These APIs have been deprecated. An exact date for removal will be confirmed before the end of 2017 but you should look to update your scripts as soon as possible.

<hr class="api-ref-rule">

```
POST /v2/usermanagement/{orgId}/products/{productId}/admin
```

Administrative rights are granted on a per-product basis.  This POST request allows you to update the administrative rights for an existing product. Use this API to grant or revoke the ProductAdmin role for one or more users.

* [Parameters](#parameters)
* [Request Body](#requestBody)
* [Responses](#responses)
* [Throttling Limits](#throttle)

## <a name="parameters" class="api-ref-subtitle">Parameters</a>
This table summarizes the parameters and how they are provided:

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include_relative partials/orgIdDescription.md %} |
| productId | path | true | The ID of the product. |
| x-api-key | header | true | {% include_relative partials/apiKeyDescription.md %} |
| Authorization | header | true | {% include_relative partials/authorizationDescription.md %} |
| Content-type | header | false | {% include_relative partials/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include_relative partials/requestIdDescription.md %} |
{:.bordertablestyle}

## <a name="requestBody" class="api-ref-subtitle">Request Body</a>

The JSON payload specifies lists of users for whom to add or remove the admin role. You only need to specify the lists you are modifying. This table summarizes the request body parameters:

| Name |   Description |
| :--- | :------- |
| addProductAdmin | A list of users that are to be granted the ProductAdmin role for this product. |
| removeProductAdmin | A list of users for whom the ProductAdmin role is to be removed for this product.  |
{:.bordertablestyle}

### Example
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

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200updateUserGroup)
- [400: Bad Request](#400updateUserGroup)
- [401: Unauthorized](#401updateUserGroup)
- [403: Forbidden](#403updateUserGroup)
- [429: Too Many Requests](#throttle)

### <a name="200updateUserGroup" class="api-ref-subtitle">200 OK</a>
The response body contains the updated product in JSON format.

{% include_relative partials/badRequest.md object="user-group" anchor="400updateUserGroup" %}

{% include_relative partials/unauthorized.md anchor="401updateUserGroup" %}

{% include_relative partials/forbidden.md anchor="403updateUserGroup" %}

## <a name="throttle" class="api-ref-subtitle">Throttling Limits</a>

{% include_relative partials/throttling.md client=5 global=50 %}
