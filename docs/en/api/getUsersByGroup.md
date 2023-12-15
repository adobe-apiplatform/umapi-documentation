---
title: Get Users by Group
layout: default
nav_link: Get Users by Group
nav_order: 413
nav_level: 3
lang: en
---
# <a name="getUsersByGroup" class="api-ref-title">Get Users in a User Group or Product Profile</a>
```
GET /v2/usermanagement/users/{orgId}/{page}/{groupName}
```
Gets a paged list of users in a specific group of an organization along with information about them. Groups can be named user groups, product profiles, or group-specific administrative groups.

For product profiles: 
* Pass the `directOnly` flag to return only those users who have a direct membership in the product profile.
* Pass the `status` parameter to return only those users who have the "active" or "inactive" status in the product profile.

__Throttle Limits__: Maximum 25 requests per minute per a client. See [Throttling Limits](#getUsersByGroupThrottle) for full details.

* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#getUsersByGroupThrottle)

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include_relative partials/orgIdDescription.md %} |
| groupName | path | true | The user group, product profile name or an administrative group. For an admin group, the name can be one of the fixed groups `_org_admin`, `_deployment_admin`, or `_support_admin`; or a group-specific admin group. These are identified with a prefix on the group name `_admin_groupName` , `_product_admin_productName`, `_developer_groupName`. If the group exists but the admin group does not, an empty list is returned. |
| X-Api-Key | header | true | {% include_relative partials/apiKeyDescription.md %} |
| Authorization | header | true | {% include_relative partials/authorizationDescription.md %} |
| page | path | false | The 0-based index of the page number being requested. If greater than existing number of pages, returns the last page of users. The page size is variable with the current value returned in the X-Page-Size response header. |
| content-type | header | false | {% include_relative partials/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include_relative partials/requestIdDescription.md %} |
| directOnly | query | false | {% include_relative partials/directOnlyDescription.md %} |
| status | query | false | For product profiles only, return only active or inactive members. Pass `active` to list users that have been provisioned for the product and have an active license. Pass `inactive` to list users who have been added to the product profile but do not have an _active_ license. When not provided, lists all member users regardless of their entitlement status.|
| excludeGroups | query | false | Default value is false. When true is passed the response will exclude the `groups` array from being returned for each individual user. See [example](#getUsersWithNoGroupsExample). |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200getUsersByGroup)
- [400: Bad Request](#400getUsersByGroup)
- [401: Unauthorized](#401getUsersByGroup)
- [403: Forbidden](#403getUsersByGroup)
- [429: Too Many Requests](#getUsersByGroupThrottle)

:warning: Use only those properties that are documented in the [Response Properties](#ResponseProps) section. Additional fields can appear in the response, but should not be relied upon.

### <a name="200getUsersByGroup" class="api-ref-subtitle">200 OK</a>
A successful request returns a response body with the requested user data in JSON format. When the response contains the last paged entry, the response includes the field `lastPage : true`. If the returned page is not the last page, make additional paginated calls to retrieve the full list.

[Identity Types](glossary.md#identity) explains the different account types available.

### Headers

{% include_relative partials/pagedResponseHeaders.md object="users" %}

### Examples

<a name="getUsersExample" class="api-ref-subtitle">Response returning three members of the Document Cloud 1 group, showing their various other group memberships:</a>

```json
{
    "lastPage": false,
    "result": "success",
    "groupName": "Document Cloud 1",
    "users": [
        {
            "email": "john@example.com",
            "status": "active",
            "groups": [
                "Document Cloud 1"
            ],
            "username": "john",
            "domain": "example.com",
            "country": "US",
            "type": "federatedID",
            "tags": [
                "edu_student"
            ]
        },
        {
            "email": "jane@example.com",
            "status": "active",
            "groups": [
                "Document Cloud 1",
                "Support for AEM Mobile",
                "_admin_Document Cloud 1",
                "_admin_Support for AEM Mobile",
                "_admin_Default Support profile",
                "_admin_Creative Cloud 1",
                "_deployment_admin",
                "_developer_Document Cloud 1"
            ],
            "username": "jane",
            "domain": "example.com",
            "country": "US",
            "type": "federatedID"
        },
        {
            "email": "bob@example.com",
            "status": "active",
            "groups": [
                "Document Cloud 1",
                "Creative Cloud 1"
            ],
            "username": "bob",
            "domain": "example.com",
            "country": "US",
            "type": "federatedID"
        }
        ...
      ]
}
```

<a name="getUsersWithNoGroupsExample" class="api-ref-subtitle">Response returning three members of the Document Cloud 1 group. The `groups` array for each user has been excluded in the response as the query parameter `excludeGroups=true` was included:</a>

```json
{
    "lastPage": false,
    "result": "success",
    "groupName": "Document Cloud 1",
    "users": [
        {
            "email": "john@example.com",
            "status": "active",
            "username": "john",
            "domain": "example.com",
            "country": "US",
            "type": "federatedID",
            "tags": [
                "edu_student"
            ]
        },
        {
            "email": "jane@example.com",
            "status": "active",
            "username": "jane",
            "domain": "example.com",
            "country": "US",
            "type": "federatedID"
        },
        {
            "email": "bob@example.com",
            "status": "active",
            "username": "bob",
            "domain": "example.com",
            "country": "US",
            "type": "federatedID"
        }
        ...
      ]
}
```

<a name="getUsersExampleLastPage" class="api-ref-subtitle">Response to request for the last page:

```json
{
    "lastPage": true,
    "result": "success",
    "groupName": "Document Cloud 1",
    "users": [
        {
            "email": "jim@example.com",
            "status": "active",
            "groups": [
                "Document Cloud 1"
            ],
            "username": "jim",
            "domain": "example.com",
            "country": "US",
            "type": "adobeID"
        }
    ]
}
```

## <a name="ResponseProps" class="api-ref-subtitle">Response Properties</a>

__result:__ _string_, The status of the request. One of `success` or an error key: `{ "success", "error", "error.apikey.invalid", "error.user.email.invalid", "error.api.user.not.parent.org", "error.organization.invalid_id" }`  
  
__message:__ _string_ An error message, returned only if initial validation of the request fails. It is not populated when a 200 status is returned.

```json
{
  "result": "error.organization.invalid_id",
  "message": "Bad organization Id"
}
```

__users:__  Contains a list of _User_ objects. Properties that are not populated are not returned in the response. Some properties are not applicable for particular account types.
{% include_relative partials/userSchemaDescription.md %}

### Schema Model

```json
{
  "groupName": "string",
  "lastPage": boolean,
  "message": "string",
  "result": "string",
  "users": [
    {
      "country": "string",
      "domain": "string",
      "email": "string",
      "firstname": "string",
      "groups": [
        "string"
      ],
      "id": "string",
      "lastname": "string",
      "status": "string",
      "type": "string",
      "username": "string",
      "tags": [
          "string"
      ]
    }
  ]
}
```

{% include_relative partials/badRequest.md anchor="400getUsersByGroup" %}

{% include_relative partials/unauthorized.md anchor="401getUsersByGroup" %}

{% include_relative partials/forbidden.md anchor="403getUsersByGroup" %}

{% include_relative partials/notFound.md object="group" anchor="404getUsersByGroup" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
Retrieve the first page of users for group Photoshop:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/0/photoshop \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
Retrieve the fifth page of users for user group DevOps:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/4/DevOps \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Retrieve a list of active users using the `status` parameter. This query will return all direct members that have an active license for _Photoshop_.
 ```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/0/photoshop?status=active \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```

## <a name="getUsersByGroupThrottle" class="api-ref-subtitle">Throttling Limits</a>

{% include_relative partials/throttling.md client=25 global=100 %}
