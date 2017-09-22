---
title: Update User Group
layout: default
nav_link: Update User Group
nav_order: 444
nav_level: 3
lang: en
---

# <a name="updateUserGroup" class="api-ref-title">Update User Group</a>
```
PUT /v2/usermanagement/{orgId}/user-groups/{groupId}
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Request Body](#requestBody)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#throttle)

<a name="intro" class="api-ref-subtitle">Overview</a>
The PUT request allows you to update the name and description of an existing [user group](glossary.html#user-group). The user-group name and description provide the administrator a means of identifying what a particular user-group represents. 

When the exact nature of an existing group changes, a system administrator can use this API to update the name or description. For instance, the group "DevOps" might be changed to "CloudOps". This operation does not affect the group's user membership, or the group's product profile memberships.  

__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#throttle) for full details.

## <a name="parameters" class="api-ref-subtitle">Parameters</a>
This table summarizes the parameters and how they are provided:

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include_relative partials/orgIdDescription.md %} |
| groupId | path | true | The id of the user-group. |
| x-api-key | header | true | {% include_relative partials/apiKeyDescription.md %} |
| Authorization | header | true | {% include_relative partials/authorizationDescription.md %} |
| Content-type | header | false | {% include_relative partials/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include_relative partials/requestIdDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200updateUserGroup)
- [400: Bad Request](#400updateUserGroup)
- [401: Unauthorized](#401updateUserGroup)
- [403: Forbidden](#403updateUserGroup)
- [429: Too Many Requests](#throttle)

### <a name="200updateUserGroup" class="api-ref-subtitle">200 OK</a>
The response body contains the updated user-group in JSON format.  

#### Example
```json
{
  "groupId": 49371437,
  "name": "UserGroup03",
  "type": "USER_GROUP"
}
```

#### Schema Properties

__groupId:__ _integer_  
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

{% include_relative partials/badRequest.md object="user-group" anchor="400updateUserGroup" %}

{% include_relative partials/unauthorized.md anchor="401updateUserGroup" %}

{% include_relative partials/forbidden.md anchor="403updateUserGroup" %}

## <a name="requestBody" class="api-ref-subtitle">Request Body</a>

This table summarizes the request body parameters:

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------- |
| name | string | true | The name of the user-group. A string of UNICODE characters limited to 255 characters in length, including spaces. The name must be unique in the organization. |
| description | string | false | A short description of the user-group. Can consist of any UNICODE characters. Optional, but highly recommended. |
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
 curl -ivs -X PUT \
   http://usermanagement.adobe.io/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups/49371437 \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id' \
   -d '{
         "description": "HR Department",
         "name": "UserGroup03"
       }'
```

## <a name="throttle" class="api-ref-subtitle">Throttling</a>

{% include_relative partials/throttling.md client=5 global=50 %}
