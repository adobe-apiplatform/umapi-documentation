---
title: Get User Groups
layout: default
nav_link: Get User Groups
nav_order: 461
nav_level: 4
lang: en
---
# <a name="getUserGroups" class="api-ref-title">Get User Groups</a>

**DEPRECATED:** These APIs have been deprecated. Please use [Get User Groups and Product Profiles](group.md).

<hr class="api-ref-rule">

```
GET /v2/usermanagement/{orgId}/user-groups
```

Retrieves all of the user groups for the given organization. Successful queries return a 200 response whose body is a JSON response representing an array of [user groups](glossary.md#usergroup). The response is paginated and specific pages are requested by using query parameter `page=x`, where x is a number.   

__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#getUserGroupsThrottle) for full details.

* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#getUserGroupsThrottle)

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

This table summarizes the parameters and how they are provided:

| Name | Type | Required | Description |
| :------ | :------ | :---: | :------ |
| orgId | path | true | {% include_relative partials/orgIdDescription.md %} |
| groupId | path | true | The id of the user-group. |
| x-api-key | header | true | {% include_relative partials/apiKeyDescription.md %} |
| Authorization | header | true | {% include_relative partials/authorizationDescription.md %} |
| Content-type | header | false | {% include_relative partials/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include_relative partials/requestIdDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200getUserGroups)
- [400: Bad Request](#400getUserGroups)
- [401: Unauthorized](#401getUserGroups)
- [403: Forbidden](#403getUserGroups)
- [429: Too Many Requests](#getUserGroupsThrottle)

### <a name="200getUserGroups" class="api-ref-subtitle">200 OK</a>
The response body contains a list of user-groups in JSON format including the groupId, name and userCount. Please note that fields can be missing if there are no values. [User-groups can have administrators](glossary.md#usergroupAdmin) who have the ability to manage the user membership of the user-group. In these scenarios, the details of the admin group and member count will be included in the response. 

#### Headers

This table summarizes the headers that are returned:

{% include_relative partials/pagedResponseHeaders.md object="user-groups" %}

#### Example
Response with 3 user-groups including a user-group with administrators.
```json
[
  {
    "groupId": 39127441,
    "name": "TestUsergroup",
    "type": "USER_GROUP",
    "adminGroupId": "42073423",
    "adminGroupName": "39127441USERGROUP_ADMIN_GROUP_NAME_SUFFIX",
    "userCount": 2,
    "adminCount": "1"
  },
  {
    "groupId": 44815360,
    "name": "UserGroup12",
    "type": "USER_GROUP",
    "userCount": 1,
    "isReadOnly": true
  },
  {
    "groupId": 44382376,
    "name": "UserGroup6",
    "type": "USER_GROUP"
  }
]
```

#### Schema Properties

__adminCount:__ _string_ 
The number of users with administrative privileges. {% include_relative partials/mayNotBePresent.md %}

__adminGroupId:__ _string_ 
{% include_relative partials/mayNotBePresent.md %}

__adminGroupName:__ _string_ 
{% include_relative partials/mayNotBePresent.md %}

__groupId:__ _long_  

__name:__ _string_

__type:__ _string_  
The group type will always be `USER_GROUP`.

__userCount:__ _long_  
The number of users in the group. {% include_relative partials/mayNotBePresent.md %}

__isReadOnly:__ _boolean_
Indicates if it is possible to directly add and remove users from the group. Further information is available at [Share User Groups](https://www.adobe.com/go/user_group_share)

#### Schema Model

```json
[
  {
    "adminCount": "string",
    "adminGroupId": "string",
    "adminGroupName": "string",
    "groupId": long,
    "name": "string",
    "type": "string",
    "userCount": long
  }
]
```

{% include_relative partials/badRequest.md anchor="400getUserGroups" %}

{% include_relative partials/unauthorized.md anchor="401getUserGroups" %}

{% include_relative partials/forbidden.md anchor="403getUserGroups" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
Retrieve the first page of user-groups:
```
curl -ivs -X GET \
   http://usermanagement.adobe.io/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id'
```

Retrieve the 3rd page of user-groups:
```
curl -ivs -X GET \
   http://usermanagement.adobe.io/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups?page=3 \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id'
```

## <a name="getUserGroupsThrottle" class="api-ref-subtitle">Throttling Limits</a>

{% include_relative partials/throttling.md client=5 global=50 %}
