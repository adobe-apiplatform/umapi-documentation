---
title: Get Users in Group
layout: default
nav_link: Get Users in Group
nav_order: 436
nav_level: 3
lang: en
---
# <a name="getUsersByGroup" class="api-ref-title">Get Users in Group</a>

```
GET /v2/usermanagement/users/{orgId}/{page}/{groupName}
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#getUsersRESTThrottle)

<a name="intro" class="api-ref-subtitle"></a>
Get a paged list of users in a specific group of an organization along with information about them. If you pass the `directOnly` flag then only users that have a direct membership to the group will be returned.  

__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#getUsersByGroupThrottle) for full details.

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| groupName | path | true | The user group or product profile name. |
| X-Api-Key | header | true | {% include apiRef/apiKeyDescription.md %} |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| page | path | false | The page number being requested. Page numbers greater than what exist will return the last page of users. |
| content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
| directOnly | query | false | {% include apiRef/directOnlyDescription.md %} |
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

[Identity Types](glossary.html#identity) explains the different account types available.

#### Headers

{% include apiRef/pagedResponseHeaders.md object="users" %}

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
                "Default Support configuration",
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
        },
```
<a name="getUsersExampleLastage" class="api-ref-subtitle">Response that is the last page:
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
The status of the request. This property can be used to manage error handling as the value will either be `success` or a corresponding error.

__user:__  
Represents a _User_ object. Properties that are not populated __will not__ be returned in the response. Some properties are not applicable for particular account types.

* **adminRoles:** _string[]_; The list of groups or roles that the user holds an administrative role. {% include apiRef/rolesDescription.md %}
* __country:__ _string_; A valid ISO 2-character country code.
* __domain:__ _string_; The user's domain.
* __email:__ _string_
* __firstname:__ _string_
* __groups:__ _string[]_; The list of groups that the user is a current member of including user-groups and product profiles. See [Groups example](#getUserGroupsExample).
* __id:__ _string_
* __lastname:__ _string_
{% include apiRef/statusDescription.md %}
* __type:__ _string_, possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.html#identity) for more information.
* __username:__ _string_; The user's username (applicable for [Enterprise](glossary.html#enterpriseId) and [Federated](glossary.html#federatedId) users). For most Adobe ID users, this value will be the same as the email address.

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

{% include apiRef/badRequest.md anchor="400getUsersByGroup" %}

{% include apiRef/unauthorized.md anchor="401getUsersByGroup" %}

{% include apiRef/forbidden.md anchor="403getUsersByGroup" %}

{% include apiRef/notFound.md object="group" anchor="404getUsersByGroup" %}

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

## <a name="getUsersByGroupThrottle" class="api-ref-subtitle">Throttling</a>

{% include apiRef/throttling.md client=25 global=100 %}
