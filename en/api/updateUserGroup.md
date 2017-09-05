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

<a name="intro" class="api-ref-subtitle"></a>
Enables the updating of the name and/or description of an existing [user-group](glossary.html#user-group). The user-group name and description provide the administrator a means of identifying what a particular user-group represents. When the exact nature of an existing group changes a system administrator may wish to update the user-group with a new name or description. For instance the group "DevOps" might be changed to "CloudOps". As the user-group `groupId` is the identifier, this operation will not affect users who are already a member of the user-group or their access to any associated product configurations.  

__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#throttle) for full details.

## <a name="parameters" class="api-ref-subtitle">Parameters</a>
This table summarizes the parameters and how they are provided:

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| groupId | path | true | The id of the user-group. |
| x-api-key | header | true | {% include apiRef/apiKeyDescription.md %} |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| Content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
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

{% include apiRef/badRequest.md object="user-group" anchor="400updateUserGroup" %}

{% include apiRef/unauthorized.md anchor="401updateUserGroup" %}

{% include apiRef/forbidden.md anchor="403updateUserGroup" %}

## <a name="requestBody" class="api-ref-subtitle">Request Body</a>

This table summarizes the request body parameters:

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------- |
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

{% include apiRef/throttling.md client=5 global=50 %}