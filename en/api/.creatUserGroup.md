---
title: Create User Group
layout: default
nav_link: Create User Group
nav_order: 443
nav_level: 3
lang: en
---

# <a name="createUserGroup" class="api-ref-title">Create User Group</a>

```
POST /v2/usermanagement/{orgId}/user-groups
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Request Body](#requestBody)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#throttle)

<a name="intro" class="api-ref-subtitle"></a>
Creates a new [user-group](glossary.html#user-group) with the specified group name and/or description in the organization. The response includes the name and description and the Adobe assigned user-group ID. Subsequent operations on the user-group will be made by reference to the group id. Upon successful completion of the request, the new user-group will be then be available for association with products and user assignment.   

__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#throttle) for full details.

## <a name="parameters" class="api-ref-subtitle">Parameters</a>
This table summarizes the parameters and how they are provided:

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| x-api-key | header | true | {% include apiRef/apiKeyDescription.md %} |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| Content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200createUserGroup)
- [400: Bad Request](#400createUserGroup)
- [401: Unauthorized](#401createUserGroup)
- [403: Forbidden](#403createUserGroup)
- [429: Too Many Requests](#throttle)

### <a name="200createUserGroup" class="api-ref-subtitle">200 OK</a>
The response body contains the created user-group in JSON format including the Adobe generated `groupId`.  

#### Example
```json
{
  "groupId": 49371437,
  "name": "UserGroup02",
  "type": "USER_GROUP"
}
```

#### Schema Properties

__groupId:__ _long_ 
Adobe generated groupId. 

__name:__ _string_

__type:__ _string_  
The group type which will always be `USER_GROUP`.

#### Schema Model

```json
{
    "groupId": long,
    "name": "string",
    "type": "string"
  }
```

{% include apiRef/badRequest.md object="user-group" anchor="400createUserGroup" %}

{% include apiRef/unauthorized.md anchor="401createUserGroup" %}

{% include apiRef/forbidden.md anchor="403createUserGroup" %}

## <a name="requestBody" class="api-ref-subtitle">Request Body</a>

This table summarizes the request body parameters:

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| name | string | true | The name of the user-group conforming to the following rule: UNICODE* characters including spaces limited to 255 characters in length. The name must be unique in the organization. |
| description | string | false | A short description of the user-group. Can consist of any UNICODE characters. This is an optional parameter but highly recommended to include. |
{:.bordertablestyle}

### Example

```json
{
 "description": "User-group Description",
 "name": "User-Group Name"
}
```

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
```
 curl -ivs -X POST \
   http://usermanagement.adobe.io/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id' \
   -d '{
         "description": "UserGroup02 Description",
         "name": "UserGroup02"
       }'
```

## <a name="throttle" class="api-ref-subtitle">Throttling</a>

{% include apiRef/throttling.md client=5 global=50 %}