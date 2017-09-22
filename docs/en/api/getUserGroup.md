---
title: Get User Group
layout: default
nav_link: Get User Group
nav_order: 442
nav_level: 3
lang: en
---

# <a name="getUserGroup" class="api-ref-title">Get User Group</a>

```
GET /v2/usermanagement/{orgId}/user-groups/{groupId}
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#throttle)

<a name="intro" class="api-ref-subtitle"></a>
This API retrieves the details of a single [user-group](glossary.html#user-group) within a specified organization by searching for them using their `groupId`. Successful queries will return a 200 response whose body is a single JSON response representing the user-group information.

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

- [200: OK](#200getUserGroup)
- [400: Bad Request](#400getUserGroup)
- [401: Unauthorized](#401getUserGroup)
- [403: Forbidden](#403getUserGroup)
- [429: Too Many Requests](#throttle)

### <a name="200getUserGroup" class="api-ref-subtitle">200 OK</a>

The response body contains the specified user-group in JSON format including the groupId, name and userCount. Please note that fields can be missing if there are no values, i.e. there are no users so `userCount` will not be returned. [User-groups can have administrators](glossary.html#usergroupAdmin) who have the ability to manage the user membership of the user-group. In these scenarios, the details of the admin group and admin member count will be included in the response. 

#### Example
```json
{
  "groupId": 39127441,
  "name": "TestUsergroup",
  "type": "USER_GROUP",
  "adminGroupId": "42073423",
  "adminGroupName": "39127441USERGROUP_ADMIN_GROUP_NAME_SUFFIX",
  "userCount": 2,
  "adminCount": "1"
}
```

#### Schema Properties

__adminCount:__ _string_  
The number of users with administrative privileges.

__adminGroupId:__ _string_ 

__adminGroupName:__ _string_  

__groupId:__ _integer_  

__name:__ _string_

__type:__ _string_  
The group type which will always be `USER_GROUP`.

__userCount:__ _integer_  
The number of users in the group.

#### Schema Model

```json
{
    "adminCount": "string",
    "adminGroupId": "string",
    "adminGroupName": "string",
    "groupId": integer,
    "name": "string",
    "type": "string",
    "userCount": integer
  }
```

{% include_relative partials/badRequest.md anchor="400getUserGroup" %}

{% include_relative partials/unauthorized.md anchor="401getUserGroup" %}

{% include_relative partials/forbidden.md anchor="403getUserGroup" %}

{% include_relative partials/notFound.md object="user-group" anchor="404getUserGroup" %}

```
< HTTP/1.1 404 Not Found
< Content-Type: application/json
< Date: Thu, 22 Jun 2017 09:39:06 GMT
< Vary: Accept-Encoding
< X-Request-Id: user-assigned-request-id
< Content-Length: 64
< Connection: keep-alive
<
{"errorMessage":"GROUP_NOT_FOUND","errorCode":"GROUP_NOT_FOUND"}
```

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
```
 curl -ivs -X GET \
   http://usermanagement.adobe.io/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups/39127441 \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id' \
```

## <a name="throttle" class="api-ref-subtitle">Throttling</a>

{% include_relative partials/throttling.md client=5 global=50 %}
