---
title: Manage User Groups
layout: default
nav_link: Manage User Groups
nav_order: 442
nav_level: 3
lang: en
---
# User Groups

The following set of APIs allow users to perform management of their organization's [user-groups](glossary.html#usergroup). Management operations include create, read, update and delete for user-groups.
_User-groups_ can be used to organize related users together and assign them to products. A user-group is a collection of different users that share a set of permissions. There are various permissions across different products that have to be assigned to many users in varying order. Managing permissions by user is not a sustainable model. The purpose of these APIs is to managing the user-groups. To associate user-groups with product configurations or users please see [Action API](ActionsRef.html).

* [Get User Groups](#getUserGroups)
* [Get User Group](getUserGroup)
* [Create User Group](#createUserGroup)
* [Update User Group](#updateUserGroup)
* [Delete User Group](#deleteUserGroup)

<hr class="api-ref-rule">

<a class="api-ref-title" name="getUserGroups">GET /v2/usermanagement/{orgId}/user-groups</a>

This API returns all the user-groups for the given organization. Successful queries will return a 200 response whose body is a JSON response representing an array of [user-groups](glossary.html#usergroup). The response is paginated and specific pages are requested by using query parameter `page=x`, where x is a number.   

### Example Requests:
Retrieve the first page of user-groups:
```
 curl -ivs -X GET \
   http://usermanagement.adobe.io/jil-api/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id' \
   -H 'x-api-key: jilservice_admin1' 
 ```
 Retrieve the 3rd page of user-groups:
 ```
 curl -ivs -X GET \
   http://usermanagement.adobe.io/jil-api/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups?page=3 \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id' \
   -H 'x-api-key: jilservice_admin1' 
 ```

## Parameters

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Req? |
| :--- | :------ | :--- | :--- | --- |
| orgId | {% include apiRef/orgIdDescription.md %} | path | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | true |
| page | The page number being requested. Page numbers greater than what exist will return the last page of user-groups. | query | false |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
{:.bordertablestyle}

## Throttling

{% include apiRef/throttling.md client=5 global=50 %}

## Responses

__Content-Type:__ _application/json_

### 200 OK
The response body contains a list of user-groups in JSON format including the groupId, name and userCount. Please note that fields can be missing if there are no values, i.e. there are no users so `userCount` will not be returned. User-groups can have administrators who have the ability to manage the user membership of the user-group. In these scenarios the details of the admin group and member count will be included in the response. 

#### Headers

This table summarizes the headers that are returned:

| Header |	Description |
| :------ | :------------- |
| X-Total-Count | The total count of user-groups being returned across all pages. |	
| X-Page-Count | The count of pages which could be fetched with the criteria specified. |	
| X-Current-Page | The page being returned. |
| X-Page-Size | The number of entries in the page being returned. |
{:.bordertablestyle}

_please note that all of the above headers are strings_

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
    "userCount": 1
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
The number of users with administrative privileges.

__adminGroupId:__ _string_ 

__adminGroupName:__ _string_ 

__groupId:__ _integer_  

__name:__ _string_

__type:__ _string_  
The group type will always be `USER_GROUP`.

__userCount:__ _integer_  
The number of users in the group.

#### Schema Model

```json
[
  {
    "adminCount": "string",
    "adminGroupId": "string",
    "adminGroupName": "string",
    "groupId": integer,
    "name": "string",
    "type": "string",
    "userCount": integer
  }
]
```

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}

<hr class="api-ref-rule">

<a name="getUserGroup" class="api-ref-title">GET /v2/usermanagement/{orgId}/user-groups/{groupId}</a>

This API retrieves the details of a single [user-group](glossary.html#user-group) within a specified organization by searching for them using their `groupId`. Successful queries will return a 200 response whose body is a single JSON response representing the user-group information.   

### Example Request:
```
 curl -ivs -X GET \
   http://usermanagement.adobe.io/jil-api/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups/39127441 \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id' \
   -H 'x-api-key: jilservice_admin1' 
```

## Parameters

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Data Type| Req? |
| :--- | :------ | :---| :--- | ---: |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| groupId | The id of the user-group. | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
{:.bordertablestyle}

## Throttling

{% include apiRef/throttling.md client=5 global=50 %}

## Responses

__Content-Type:__ _application/json_

### 200 OK

The response body contains the specified user-group in JSON format including the groupId, name and userCount. Please note that fields can be missing if there are no values, i.e. there are no users so `userCount` will not be returned. User-groups can have administrators who have the ability to manage the user membership of the user-group. In these scenarios the details of the admin group and admin member count will be included in the response. 

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

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}

{% include apiRef/notFound.md object="user-group" %}
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
<hr class="api-ref-rule">
<a name="createUserGroup" class="api-ref-title">POST /v2/usermanagement/{orgId}/user-groups</a>

Creates a new [user-group](glossary.html#user-group) with the specified group name and/or description in the organization. The response includes the name and description and the Adobe assigned user-group ID. Subsequent operations on the user-group will be made by reference to the group id. Upon successful completion of the request, the new user-group will be then be available for association with products and user assignment.   

### Example Request:
```
 curl -ivs -X POST \
   http://usermanagement.adobe.io/jil-api/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id' \
   -H 'x-api-key: jilservice_admin1' \
   -d '{
         "description": "UserGroup02 Description",
         "name": "UserGroup02"
       }'
```

## Parameters

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Data Type| Req? |
| :--- | :------ | :---| :--- | ---: |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
{:.bordertablestyle}

## Request Body

This table summarizes the request body parameters:

| Name | Description | Type| Req? |
| :--- | :------ | :--- | ---: |
| name | The name of the user-group conforming to the following rule: UNICODE* characters including spaces limited to 255 characters in length. The name must be unique in the organization. | string | true |
| description | A short description of the user-group. Can consist of any UNICODE characters. This is an optional parameter but highly recommended to include. | string | false |
{:.bordertablestyle}

### Example

```json
{
 "description": "User-group Description",
 "name": "User-Group Name"
}
```

## Throttling

{% include apiRef/throttling.md client=5 global=50 %}

## Responses

__Content-Type:__ _application/json_

### 200 OK
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

__groupId:__ _integer_ 
Adobe generated groupId. 

__name:__ _string_

__type:__ _string_  
The group type which will always be `USER_GROUP`.

#### Schema Model

```json
{
    "groupId": integer,
    "name": "string",
    "type": "string"
  }
```

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}

<hr class="api-ref-rule">
<a name="updateUserGroup" class="api-ref-title">PUT /v2/usermanagement/{orgId}/user-groups/{groupId}</a>

Enables the updating of the name and/or description of an existing [user-group](glossary.html#user-group). The user-group name and description provide the administrator a means of identifying what a particular user-group represents. When the exact nature of an existing group changes a system administrator may wish to update the user-group with a new name or description. For instance the group "DevOps" might be changed to "CloudOps". As the user-group `groupId` is the identifier, this operation will not affect users who are already a member of the user-group or their access to any associated product configurations.  

### Example Request:
```
 curl -ivs -X PUT \
   http://usermanagement.adobe.io/jil-api/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups/49371437 \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id' \
   -H 'x-api-key: jilservice_admin1' \
   -d '{
         "description": "HR Department",
         "name": "UserGroup03"
       }'
```
## Parameters

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Data Type| Req? |
| :--- | :------ | :---| :--- | ---: |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| groupId | The id of the user-group. | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
{:.bordertablestyle}

## Request Body

This table summarizes the request body parameters:

| Name | Description | Type| Req? |
| :--- | :------ | :--- | ---: |
| name | The name of the user-group conforming to the following rule: UNICODE* characters including spaces limited to 255 characters in length. The name must be unique in the organization. | string | true |
| description | A short description of the user-group. Can consist of any UNICODE characters. This is an optional parameter but highly recommended to include. | string | false |
{:.bordertablestyle}

### Example

```json
{
 "description": "User-group Description",
 "name": "User-Group Name"
}
```

## Throttling

{% include apiRef/throttling.md client=5 global=50 %}

## Responses

__Content-Type:__ _application/json_

### 200 OK
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
    "groupId": integer,
    "name": "string",
    "type": "string"
  }
```

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}

<hr class="api-ref-rule">
<a name="deleteUserGroup" class="api-ref-title">DELETE /v2/usermanagement/{orgId}/user-groups/{groupId}</a>

Permanently delete a [user-group](glossary.html#user-group) identified by the `groupId` from the given organization. When you remove a user-group, the users in that group are still retained in the Admin Console. However, if you have assigned product profiles to this group, then the users in the group will no longer have access to the associated products.

### Example Request:
```
 curl -ivs -X DELETE \
   http://usermanagement.adobe.io/jil-api/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups/49371437 \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id' \
   -H 'x-api-key: jilservice_admin1'
```
## Parameters

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Data Type| Req? |
| :--- | :------ | :---| :--- | ---: |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| groupId | The id of the user-group. | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
{:.bordertablestyle}

## Throttling

{% include apiRef/throttling.md client=5 global=50 %}

## Responses

__Content-Type:__ _application/json_

### 204 No Content
The user-group has been successfully deleted and no longer exists.  

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}