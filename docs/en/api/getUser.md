---
title: Get User Information
layout: default
nav_link: Get User Information
nav_order: 411
nav_level: 3
lang: en
---
# <a name="getUserInfo" class="api-ref-title">Get User Information</a>
```
GET /v2/usermanagement/organizations/{orgId}/users/{userString}
```
Retrieves the details of a single user within a specified organization, identified by email address or username and domain. Successful queries return a 200 response whose body is a single JSON structure containing the user information.

__Throttle Limits__: Maximum 25 requests per minute per a client. See [Throttling Limits](#getUserThrottle) for full details.

* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#getUserThrottle) 

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Req? | Description |
| :---- | :--- | :---: | :------ |
| orgId | path | true | {% include_relative partials/orgIdDescription.md %} |
| userString | path | true | For [AdobeID](glossary.md#adobeId), [Enterprise](glossary.md#enterpriseId) and _[email-federated](glossary.md#federatedId)_ users this should be the full email address including domain. In all cases the parameter is case-insensitive. [Identity Types](glossary.md#identity) explains the different account types available. |
| X-Api-Key | header | true | {% include_relative partials/apiKeyDescription.md %} |
| Authorization | header | true | {% include_relative partials/authorizationDescription.md %} |
| domain | query | false | Optional parameter but highly recommended including for all user types. For [AdobeID](glossary.md#adobeId) users this would be `AdobeID`. For [Enterprise](glossary.md#enterpriseId) and _[email-federated](glossary.md#federatedId)_ users the domain will either match the email domain or, in the case of multi-domain federations, have any other domain for that directory. |
| content-type | header | false | {% include_relative partials/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include_relative partials/requestIdDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200getUser)
- [400: Bad Request](#400getUser)
- [401: Unauthorized](#401getUser)
- [403: Forbidden](#403getUser)
- [429: Too Many Requests](#getUserThrottle)

:warning: Use only those properties that are documented in the [Response Properties](#ResponseProps) section. Additional fields can appear in the response, but should not be relied upon.

### <a name="200getUser" class="api-ref-subtitle">200 OK</a>
The response body contains the requested user data in JSON format including any of the user's group membership and admin roles. Fields can be missing if values were never supplied or are not applicable for a particular account type.

[Identity Types](glossary.md#identity) explains the different account types available.

### Examples
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
    "groups": [
      "_org_admin"
    ]
  }
}
```

<a name="getUserGroupsExample" class="api-ref-subtitle">[Enterprise](glossary.md#enterpriseId) User with membership</a> in two user-groups but no administrative roles. If the fields are not populated (`firstname` and`lastname` in this example), they are excluded from the response.
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
[Federated](glossary.md#federatedId) User with no memberships or administrative roles:
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
## <a name="ResponseProps" class="api-ref-subtitle">Response Properties</a>

__result:__ _string_, The status of the request. One of `success` or an error key: `{ "success", "error", "error.apikey.invalid", "error.user.email.invalid", "error.api.user.not.parent.org", "error.organization.invalid_id" }`  
  
__message:__ _string_ An error message, returned only if initial validation of the request fails. It is not populated when a 200 status is returned.

```json
{
  "result": "error.organization.invalid_id",
  "message": "Bad organization Id"
}
```

__user:__  A _user_ object containing relevant properties. Properties that are not populated are not returned in the response. Some properties are not applicable for particular account types.
{% include_relative partials/userSchemaDescription.md %}

### Schema Model

```json
{
  "message": "string",
  "result": "string",
  "user": {
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

{% include_relative partials/badRequest.md anchor="400getUser" %}

{% include_relative partials/unauthorized.md anchor="401getUser" %}

{% include_relative partials/forbidden.md anchor="403getUser" %}

{% include_relative partials/notFound.md object="user" anchor="404getUser" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
Searching by email for [AdobeID](glossary.md#adobeId), [Enterprise](glossary.md#enterpriseId) or [email-federated](glossary.md#federatedId) users:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
Searching for [AdobeID](glossary.md#adobeId) user with domain:
```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com?domain=AdobeID \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
 Searching for [Enterprise](glossary.md#enterpriseId) or [email-federated](glossary.md#federatedId) users with domain parameter included:
```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com?domain=example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
Note that the authorization directory, which is specified by the "domain" parameter, can contain more than one domain name.
This means that the "domain" value does not necessarily match the domain portion of user email addresses.

## <a name="getUserThrottle" class="api-ref-subtitle">Throttling Limits</a>

{% include_relative partials/throttling.md client=25 global=100 %}
