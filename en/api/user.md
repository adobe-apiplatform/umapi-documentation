---
title: Manage Users
layout: default
nav_link: Manage Users
nav_order: 441
nav_level: 3
lang: en
---

# Manage Users

An application can use the User Management API to access Adobe users and manage their identities. You can create and remove user accounts for your organization, modify a user’s personal information (depending on the account type), and modify users’ access rights to Adobe applications within your organization.

* [Get a User](#getUserByEmailOrUsername)
* [Add a User](ActionsRef.html)
* [Update a User](ActionsRef.html)

<hr class="api-ref-rule">

<a name="getUserByEmailOrUsername" class="api-ref-title">GET /v2/usermanagement/organizations/{orgId}/users/{userString}</a>

This API retrieves the details of a single user within a specified organization by searching for them using their email address or a username and domain combo. Successful queries will return a 200 response whose body is a single JSON response representing the user information.  

### Example Requests:
Searching by email for Type 1, Type 2 or Type 3 email-federated users:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Searching by username for Type 3 username-federated users:
 ```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe?domain=example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Searching for Type 1 user with domain:
 ```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com?domain=AdobeID \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Searching for Type 2 or Type 3 email-federated users with domain parameter included:
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
___

## Parameters

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Data Type | Req? |
| :---- | :------ | :--- | :--- | ---: |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| userString | For Type 1, Type 2 and Type 3 _email-federated_ users this should be the full email address including domain. For Type 3 _username-federated_ users, this should be the username. In both cases the parameter is case-insensitive. | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| domain | Optional parameter but highly recommended including for all user types. For Type 1 users this would be `AdobeID`. For Type 2 and Type 3 _email-federated_ users the domain will either match the email domain or, in the case of multi-domain federations, have any other domain for that directory. For Type 3 _username-federated_ users the value must be a claimed domain which contains the user's account | query | string | false |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
{:.bordertablestyle}

___

## Responses

__Content-Type:__ _application/json_

### 200 OK
The response body contains the requested user data in JSON format including any of the user's group membership and admin roles. Fields can be missing if values were never supplied or are not applicable for a particular account type.

[Identity Types](glossary.html#identity) explains the different account types available.

#### Examples
<a name="getUserAdminRolesExample" class="api-ref-subtitle">Response for an Adobe ID (Type 1) with System Administrator role:</a>
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
<a name="getUserGroupsExample" class="api-ref-subtitle">Enterprise User (Type 2) with membership</a> to 2 user-groups but no administrative roles. If the fields are not populated e.g. `firstname`/`lastname` in this example, then they will be excluded from the response.
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
Federated User (Type 3) with no memberships or administrative roles:
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
* __groups:__ _string[]_; The list of groups that the user is a current member of including user-groups and product configurations. See [Groups example](#getUserGroupsExample).
* __id:__ _string_
* __lastname:__ _string_
* __status:__ _string_, possible values:`{ "active", "disabled", "locked", "removed" }`; The current status of the user:
  * active: Normal status for a user account in good standing.
  * disabled: Disabled temporarily - not removed, but the user will not be allowed to login.
  * locked: Disabled permanently - not removed, user will not be allowed to login.
  * removed: The user account is being removed. 
* __type:__ _string_, possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.html#identity) for more information.
* __username:__ _string_; The user's username (applicable for enterprise and federated users). For most Type 1 users, this value will be the same as the email address.

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

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}

{% include apiRef/notFound.md object="user" %}