---
title: Manage Users
layout: default
nav_link: Get User in Organization
nav_order: 432
nav_level: 3
lang: en
---

# <a name="getUserByEmailOrUsername" class="api-ref-title">Get User in Organization</a>

```
GET /v2/usermanagement/organizations/{orgId}/users/{userString}
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#getUserThrottle)

<a name="intro" class="api-ref-subtitle"></a>
This API retrieves the details of a single user within a specified organization by searching for them using their email address or a username and domain combo. Successful queries will return a 200 response whose body is a single JSON response representing the user information.

__Throttle Limits__: Maximum 25 requests per minute per a client. See [Throttling Limits](#getUserThrottle) for full details.  

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Req? | Description |
| :---- | :--- | :---: | :------ |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| userString | path | true | For [AdobeID](glossary.html#adobeId), [Enterprise](glossary.html#enterpriseId) and _[email-federated](glossary.html#federatedId)_ users this should be the full email address including domain. For _[username-Federated](glossary.html#federatedId)_ users, this should be the username. In both cases the parameter is case-insensitive. [Identity Types](glossary.html#identity) explains the different account types available. |
| X-Api-Key | header | true | {% include apiRef/apiKeyDescription.md %} |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| domain | query | false | Optional parameter but highly recommended including for all user types. For [AdobeID](glossary.html#adobeId) users this would be `AdobeID`. For [Enterprise](glossary.html#enterpriseId) and _[email-federated](glossary.html#federatedId)_ users the domain will either match the email domain or, in the case of multi-domain federations, have any other domain for that directory. For _[username-federated](glossary.html#federatedId)_ users the value must be a claimed domain which contains the user's account |
| content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200getUser)
- [400: Bad Request](#400getUser)
- [401: Unauthorized](#401getUser)
- [403: Forbidden](#403getUser)
- [429: Too Many Requests](#getUserThrottle)

### <a name="200getUser" class="api-ref-subtitle">200 OK</a>
The response body contains the requested user data in JSON format including any of the user's group membership and admin roles. Fields can be missing if values were never supplied or are not applicable for a particular account type.

[Identity Types](glossary.html#identity) explains the different account types available.

#### Examples
<a name="getUserAdminRolesExample" class="api-ref-subtitle">Response for an Adobe ID user with System Administrator role:</a>
```json
{
  "result": "success",
  "user": {
    "email": "jdoe@my-domain.com",
    "status": "active",
    "username": "jdoe@my-domain.com",
    "domain": "my-domain.com",
    "firstname": "John",
    "lastname": "Doe",
    "country": "US",
    "type": "adobeID",
    "adminRoles": [
      "org"
    ]
  }
}
```
<a name="getUserGroupsExample" class="api-ref-subtitle">[Enterprise](glossary.html#enterpriseId) User with membership</a> to 2 user-groups but no administrative roles. If the fields are not populated e.g. `firstname`/`lastname` in this example, then they will be excluded from the response.
```json
{
  "result": "success",
  "user": {
    "email": "jdoe@my-domain.com",
    "status": "active",
    "groups": [
      "UserGroup1",
      "UserGroup2"
    ],
    "username": "jdoe@my-domain.com",
    "domain": "my-domain.com",
    "country": "JP",
    "type": "enterpriseID"
  }
}
```
[Federated](glossary.html#federatedId) User with no memberships or administrative roles:
```json
{
  "result": "success",
  "user": {
    "email": "jdoe@my-domain.com",
    "status": "active",
    "username": "johndoe",
    "domain": "my-domain.com",
    "firstname": "John",
    "lastname": "Doe",
    "country": "US",
    "type": "federatedID"
  }
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

* **adminRoles:** _string[]_; The list of groups or roles that the user holds an administrative role. For example if a user is an System Administrator then `org` will be returned. If the user is an administrator for a user-group or product, the name of the group will be returned. See [AdminRoles example](#getUserAdminRolesExample).
* __country:__ _string_; A valid ISO 2-character country code.
* __domain:__ _string_; The user's domain.
* __email:__ _string_
* __firstname:__ _string_
* __groups:__ _string[]_; The list of groups that the user is a current member of including user-groups and product profiles. See [Groups example](#getUserGroupsExample).
* __id:__ _string_
* __lastname:__ _string_
{% include apiRef/statusDescription.md %}
* __type:__ _string_, possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.html#identity) for more information.
* __username:__ _string_; The user's username (applicable for [Enterprise](glossary.html#enterpriseId) and [Federated](glossary.html#federatedId) users). For most [AdobeID](glossary.html#adobeId) users, this value will be the same as the email address.

#### Schema Model

```json
{
  "message": "string",
  "result": "string",
  "user": {
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
}
```

{% include apiRef/badRequest.md anchor="400getUser" %}

{% include apiRef/unauthorized.md anchor="401getUser" %}

{% include apiRef/forbidden.md anchor="403getUser" %}

{% include apiRef/notFound.md object="user" anchor="404getUser" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
Searching by email for [AdobeID](glossary.html#adobeId), [Enterprise](glossary.html#enterpriseId) or [email-federated](glossary.html#federatedId) users:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
 Searching by username for [username-federated](glossary.html#federatedId) users:
```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe?domain=example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
 Searching for [AdobeID](glossary.html#adobeId) user with domain:
```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com?domain=AdobeID \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
 Searching for [Enterprise](glossary.html#enterpriseId) or [email-federated](glossary.html#federatedId) users with domain parameter included:
```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com?domain=example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
 Searching for users in a multi-domain directory:
```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com?domain=my-domain.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```

## <a name="getUserThrottle" class="api-ref-subtitle">Throttling</a>

{% include apiRef/throttling.md client=25 global=100 %}