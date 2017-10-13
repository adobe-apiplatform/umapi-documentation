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
Gets a paged list of users in a specific group of an organization along with information about them. If you pass the `directOnly` flag, only users that have a direct membership to the group are returned.  
__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#getUsersByGroupThrottle) for full details.

* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#getUsersByGroupThrottle)

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include_relative partials/orgIdDescription.md %} |
| groupName | path | true | The user group or product profile name. |
| X-Api-Key | header | true | {% include_relative partials/apiKeyDescription.md %} |
| Authorization | header | true | {% include_relative partials/authorizationDescription.md %} |
| page | path | false | The page number being requested. If greater than existing number of pages, returns the last page of users. |
| content-type | header | false | {% include_relative partials/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include_relative partials/requestIdDescription.md %} |
| directOnly | query | false | {% include_relative partials/directOnlyDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200getUsersByGroup)
- [400: Bad Request](#400getUsersByGroup)
- [401: Unauthorized](#401getUsersByGroup)
- [403: Forbidden](#403getUsersByGroup)
- [429: Too Many Requests](#getUsersByGroupThrottle)

### <a name="200getUsersByGroup" class="api-ref-subtitle">200 OK</a>
A successful request returns a response body with the requested user data in JSON format. When the response contains the last paged entry, the response includes the field `lastPage : true`. If the returned page is not the last page, make additional paginated calls to retrieve the full list.

[Identity Types](glossary.md#identity) explains the different account types available.

#### Headers

{% include_relative partials/pagedResponseHeaders.md object="users" %}

#### Examples

<a name="getUsersExample" class="api-ref-subtitle">Response returning three users with different group membership and administrative rights:</a>

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
            "type": "federatedID"
        },
        {
            "email": "jane@example.com",
            "status": "active",
            "groups": [
                "Document Cloud 1",
                "Support for AEM Mobile"
            ],
            "username": "jane",
            "adminRoles": [
                "deployment",
                "Document Cloud 1",
                "Support for AEM Mobile",
                "Default Support profile",
                "Creative Cloud 1"
            ],
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
```

<a name="getUsersExampleLastPage" class="api-ref-subtitle">Response that is the last page:

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

#### Schema Properties

__message:__ _string_  
Only returned if initial validation of the request fails. It is not populated when a 200 status is returned.

```json
{
  "result": "error.organization.invalid_id",
  "message": "Bad organization Id"
}
```

__result:__ _string_, possible values: `{ "success", "error", "error.apikey.invalid", "error.user.email.invalid", "error.api.user.not.parent.org", "error.organization.invalid_id" }`  
The status of the request. Can be used to manage error handling; the value is either `success` or a corresponding error.

__user:__  
Represents a _User_ object. Properties that are not populated are returned in the response. Some properties are not applicable for particular account types.

* **adminRoles:** _string[]_; The list of groups or roles that the user holds an administrative role. Possible roles include:
  * "org": The user is a [System Administrator](glossary.md#orgAdmin).
  * "deployment": The user is a [Deployment Administrator](glossary.md#deployment).
  * "{product-profile-name}": The user is a [Product Profile Administrator](glossary.md#productProfileAdmin).
  * "{user-group-name}": The user is a [UserGroup Administrator](glossary.md#usergroupAdmin).
  * "support": The user is a [Support Administator](glossary.md#supportAdmin). 
* __country:__ _string_; A valid ISO 2-character country code.
* __domain:__ _string_; The user's domain.
* __email:__ _string_
* __firstname:__ _string_
* __groups:__ _string[]_; The list of groups in which the user is a current member, including both user groups and product profiles. 
* __id:__ _string_
* __lastname:__ _string_
{% include_relative partials/statusDescription.md %}
* __type:__ _string_, possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.md#identity) for more information.
* __username:__ _string_; The user's username (applicable for [Enterprise](glossary.md#enterpriseId) and [Federated](glossary.md#federatedId) users). For most Adobe ID users, this value is the same as the email address.

#### Schema Model

```json
{
  "groupName": "string",
  "lastPage": boolean,
  "message": "string",
  "result": "string",
  "users": [
    {
      "adminRoles": [
        "string"
      ],
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
      "username": "string"
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
Retrieve the fourth page of users for user-group DevOps:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/4/DevOps \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```

## <a name="getUsersByGroupThrottle" class="api-ref-subtitle">Throttling Limits</a>

{% include_relative partials/throttling.md client=25 global=100 %}
