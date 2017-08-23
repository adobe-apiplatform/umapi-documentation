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

* [Get a User in an Organization](#getUserByEmailOrUsername)
* [Add a User to an Organization](ActionsRef.html)
* [Update an existing User in the Organization](ActionsRef.html#update)
* [Delete a User from an Organization](ActionsRef.html#removeFromOrg)
* [Get all Users in an Organization](#getUsers)
* [Get a list of members in a User Group](#getUsersByGroup)
* [Get a list of users in a Product Profile Group](#getUsersByGroup)

<hr class="api-ref-rule">

<a name="getUserByEmailOrUsername" class="api-ref-title">GET /v2/usermanagement/organizations/{orgId}/users/{userString}</a>

This API retrieves the details of a single user within a specified organization by searching for them using their email address or a username and domain combo. Successful queries will return a 200 response whose body is a single JSON response representing the user information.  

### __Example Requests__
Searching by email for AdobeID, Enterprise or email-Federated users:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Searching by username for username-federated users:
 ```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe?domain=example.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Searching for AdobeID user with domain:
 ```
 curl -X GET https://usermanagement.adobe.io/v2/usermanagement/organizations/12345@AdobeOrg/users/jdoe@example.com?domain=AdobeID \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
 Searching for Enterprise or email-federated users with domain parameter included:
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

## __Parameters__

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Data Type | Req? |
| :---- | :------ | :--- | :--- | ---: |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| userString | For AdobeID, Enterprise and _email-federated_ users this should be the full email address including domain. For _username-federated_ users, this should be the username. In both cases the parameter is case-insensitive. | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| domain | Optional parameter but highly recommended including for all user types. For AdobeID users this would be `AdobeID`. For Enterprise and _email-federated_ users the domain will either match the email domain or, in the case of multi-domain federations, have any other domain for that directory. For _username-federated_ users the value must be a claimed domain which contains the user's account | query | string | false |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
{:.bordertablestyle}

## __Responses__

__Content-Type:__ _application/json_

### __200 OK__
The response body contains the requested user data in JSON format including any of the user's group membership and admin roles. Fields can be missing if values were never supplied or are not applicable for a particular account type.

[Identity Types](glossary.html#identity) explains the different account types available.

#### __Examples__
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
<a name="getUserGroupsExample" class="api-ref-subtitle">Enterprise User with membership</a> to 2 user-groups but no administrative roles. If the fields are not populated e.g. `firstname`/`lastname` in this example, then they will be excluded from the response.
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
Federated User with no memberships or administrative roles:
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
#### __Schema Properties__

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
{% include apiRef/statusDescription.md %}
* __type:__ _string_, possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.html#identity) for more information.
* __username:__ _string_; The user's username (applicable for Enterprise and Federated users). For most AdobeID users, this value will be the same as the email address.

#### __Schema Model__

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

<hr class="api-ref-rule">
## <a name="getUsers" class="api-ref-title">Get Users</a>
UMAPI has two APIs for retrieving a list of users. The selection of which API to use can be determined by aesthetic preference and required filtering of results:
* [GET /v2/usermanagement/users/{orgId}/{page}](#getUsersWithPage)
  * Return a list of paginated users using a path parameter.
  * Filter users by domain.
  * Return a list of all the _direct only_ memberships for each user.
  * Return a list of all the _indirect_ memberships for each user.
* [GET /v2/usermanagement/{orgId}/users](#getUsersREST)
  * Return a list of paginated users using a query parameter.
  * Return a list of all the _direct only_ memberships for each user.
  * Return a list of all the _indirect_ memberships for each user.

<hr class="api-ref-rule">
<a name="getUsersWithPage" class="api-ref-title">GET /v2/usermanagement/users/{orgId}/{page}</a>

Retrieve a paged list of all users in your organization along with information about them. The number of users returned in each call is subject to change but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list of users. The `domain` query parameter filters the results to only return users within a specified domain.  

### __Example Requests__
Retrieve the first page of users:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/0 \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
Retrieve the fourth page of users:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/4 \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
Retrieve the first page of users with domain _my-domain.com_:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/4?domain=my-domain.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
Retrieve the first page of users including details of all the memberships (direct and indirect) for each user:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/1?directOnly=false \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```

## __Parameters__

This table summarizes the parameters and how they are provided:

| Name | Description | Type | Data Type | Req? |
| :--- | :------ | :--- | :--- | --- |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| page | The page number being requested. Page numbers greater than what exist will return the last page of users. | path | string | false |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
| domain | Retrieves users from a domain linked to an organization through the Trusted Domain relationship. | query | string | false |
| directOnly | {% include apiRef/directOnlyDescription.md %} | query | string | false |
{:.bordertablestyle}

## __Responses__

__Content-Type:__ _application/json_

### __200 OK__
A successful request returns a response body with the requested user data in JSON format. When the response contains the last paged entry, the response includes the field `lastPage : true`. If the returned page is not the last page, make additional paginated calls to retrieve the full list.

[Identity Types](glossary.html#identity) explains the different account types available.

#### __Headers__

This table summarizes the headers that are returned:

| Header |  Description |
| :------ | :------------- |
| X-Total-Count | The total count of user-groups being returned across all pages. | 
| X-Page-Count | The count of pages which could be fetched with the criteria specified. | 
| X-Current-Page | The page being returned. |
| X-Page-Size | The number of entries in the page being returned. |
{:.bordertablestyle}

_please note that all of the above headers are strings_

#### __Examples__
<a name="getUsersExample" class="api-ref-subtitle">Response returning three users with different group membership and administrative rights:</a>
```json
{
    "lastPage": false,
    "result": "success",
    "users": [
        {
            "email": "psmith@example.com",
            "status": "active",
            "username": "psmith",
            "adminRoles": [
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
            "email": "jane@example.com",
            "status": "active",
            "groups": [
                "Marketing Cloud 1",
                "Marketing Cloud 2",
                "Creative Cloud 1",
                "Document Cloud 1"
            ],
            "username": "jane",
            "domain": "example.com",
            "firstname": "Jane",
            "lastname": "Doe",
            "country": "US",
            "type": "federatedID"
        },
        {
            "email": "joe@example.com",
            "status": "active",
            "groups": [
                "Document Cloud 1",
                "Support for AEM Mobile"
            ],
            "username": "joe",
            "adminRoles": [
                "deployment",
                "Document Cloud 1",
                "Support for AEM Mobile",
                "Default Support configuration",
                "Creative Cloud 1"
            ],
            "domain": "example.com",
            "firstname": "First",
            "lastname": "Last",
            "country": "US",
            "type": "federatedID"
        }
    ]
}
```
<a name="getUsersExampleLastage" class="api-ref-subtitle">Response that is the last page:
```json
{
    "lastPage": true,
    "result": "success",
    "users": [
        {
            "email": "last@example.com",
            "status": "active",
            "username": "last",
            "domain": "example.com",
            "country": "US",
            "type": "federatedID"
        }
    ]
}
```

#### __Schema Properties__

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

__users:__  
Represents a list of _User_ objects. Properties that are not populated __will not__ be returned in the response. Some properties are not applicable for particular account types.

* **adminRoles:** _string[]_; The list of groups or roles that the user holds an administrative role. See [AdminRoles](#getUserAdminRolesExample) for an example of the response. {% include apiRef/rolesDescription.md %}
* __country:__ _string_; A valid ISO 2-character country code.
* __domain:__ _string_; The user's domain.
* __email:__ _string_
* __firstname:__ _string_
* __groups:__ _string[]_; The list of groups that the user is a current member of including user-groups and product configurations. See [Groups example](#getUserGroupsExample).
* __id:__ _string_
* __lastname:__ _string_
{% include apiRef/statusDescription.md %}
* __type:__ _string_, possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.html#identity) for more information.
* __username:__ _string_; The user's username (applicable for Enterprise and Federated users). For most AdobeID users, this value will be the same as the email address.

#### __Schema Model__

```json
{
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

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}

{% include apiRef/notFound.md object="domain" %}

<hr class="api-ref-rule">
<a name="getUsersREST" class="api-ref-title">GET /v2/usermanagement/{orgId}/users</a>

Retrieve a paged list of all users in your organization along with information about them. The number of users returned in each call is subject to change but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list of users.  

### __Example Requests__
Retrieve the first page of users:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/12345@AdobeOrg/users?page=0 \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```
Retrieve the fourth page of users and their direct only memberships:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/12345@AdobeOrg/users?page=4&directOnly=true \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
 ```

## __Parameters__

This table summarizes the parameters and how they are provided:

| Name | Description | Type | DataType | Req? |
| :--- | :------ | :--- | :--- | --- |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| page | The page number being requested. Page numbers greater than what exist will return the last page of users. | query | string | false |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
| directOnly | {% include apiRef/directOnlyDescription.md %} | query | string | false |
{:.bordertablestyle}

## __Responses__

__Content-Type:__ _application/json_

### __200 OK__
The response body contains a list of users in JSON format including the email, firstName and lastName. Please note that fields can be missing if there are no values, i.e. if the user is not a member of any groups then `groups` will not be returned. Use the response headers `X-Total-Count` and `X-Page-Count` to determine total number of users and total page count.

#### __Headers__

This table summarizes the headers that are returned:

| Header |  Description |
| :------ | :------------- |
| X-Total-Count | The total count of user-groups being returned across all pages. | 
| X-Page-Count | The count of pages which could be fetched with the criteria specified. | 
| X-Current-Page | The page being returned. |
| X-Page-Size | The number of entries in the page being returned. |
{:.bordertablestyle}

_please note that all of the above headers are strings_

#### __Examples__
<a name="getUsersExample" class="api-ref-subtitle">Response returning three users with different group membership and administrative rights:</a>
```json
[
    {
        "id": "4EB5B571575A6B057F000101@example.com",
        "email": "john@example.com",
        "status": "active",
        "groups": [
            "Marketing Cloud 1 - Default Access",
            "Marketing Cloud 1 - All Report Access",
            "Marketing Cloud 1 - EDITOR",
            "Marketing Cloud 1 - Default Access"
        ],
        "username": "john@example.com",
        "domain": "example.com",
        "firstName": "John",
        "lastName": "Doe",
        "countryCode": "US",
        "userType": "enterpriseID"
    },
    {
        "id": "6237573D58A4C1B90A494038@umsdkneworg1-t2example.com",
        "email": "jane@example.com",
        "status": "active",
        "username": "jane@example.com",
        "domain": "example.com",
        "firstName": "Jane",
        "lastName": "Doe",
        "countryCode": "US",
        "userType": "enterpriseID"
    },
    {
        "id": "0A0E84765756CF537F000101@example.com",
        "email": "bob@example.com",
        "status": "active",
        "groups": [
            "Document Cloud 1"
        ],
        "username": "bob@example.com",
        "domain": "example.com",
        "firstName": "Bob",
        "lastName": "James",
        "countryCode": "US",
        "userType": "enterpriseID"
    }
]
```

#### __Schema Properties__

__user:__  
Represents a _User_ object. Properties that are not populated __will not__ be returned in the response. Some properties are not applicable for particular account types. See [Identity Types](glossary.html#identity) for more information on account types.

* **adminRoles:** _string[]_; The list of groups or roles that the user holds an administrative role. {% include apiRef/rolesDescription.md %}
* __countryCode:__ _string_; A valid ISO 2-character country code.
* __domain:__ _string_; The user's domain.
* __email:__ _string_
* __firstName:__ _string_
* __groups:__ _string[]_; The list of groups that the user is a current member of including user-groups and product configurations.
* __id:__ _string_
* __lastName:__ _string_
* __phoneNumber:__ _string_
{% include apiRef/statusDescription.md %}
* __userType:__ _string_, possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.html#identity) for more information.
* __username:__ _string_; The user's username (applicable for Enterprise and Federated users). For most AdobeID users, this value will be the same as the email address.

#### __Schema Model__

```json
[
  {
    "adminRoles": [
      "string"
    ],
    "countryCode": "string",
    "domain": "string",
    "email": "string",
    "firstName": "string",
    "groups": [
      "string"
    ],
    "id": "string",
    "lastName": "string",
    "phoneNumber": "string",
    "status": "string",
    "userType": "string",
    "username": "string"
  }
]
```

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}

<hr class="api-ref-rule">

<a name="getUsersByGroup" class="api-ref-title">GET /v2/usermanagement/users/{orgId}/{page}/{groupName}</a>

Get a paged list of users in a specific group of an organization along with information about them. If you pass the `directOnly` flag then only users that have a direct membership to the group will be returned.  

### __Example Requests__
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

## __Parameters__

This table summarizes the parameters and how they are provided:

| Name | Description | Type | DataType | Req? |
| :--- | :------ | :--- | :--- | --- |
| orgId | {% include apiRef/orgIdDescription.md %} | path | string | true |
| x-api-key | {% include apiRef/apiKeyDescription.md %} | header | string | true |
| page | The page number being requested. Page numbers greater than what exist will return the last page of users. | path | string | false |
| Authorization | {% include apiRef/authorizationDescription.md %} | header | string | true |
| Content-type | {% include apiRef/contentTypeDescription.md %} | header | string | false |
| X-Request-Id | {% include apiRef/requestIdDescription.md %} | header | string | false |
| groupName | The user group or product configuration name. | path | string | true |
| directOnly | {% include apiRef/directOnlyDescription.md %} | query | string | false |
{:.bordertablestyle}

## __Responses__

__Content-Type:__ _application/json_

### __200 OK__
A successful request returns a response body with the requested user data in JSON format. When the response contains the last paged entry, the response includes the field `lastPage : true`. If the returned page is not the last page, make additional paginated calls to retrieve the full list.

[Identity Types](glossary.html#identity) explains the different account types available.

#### __Headers__

This table summarizes the headers that are returned:

| Header |  Description |
| :------ | :------------- |
| X-Total-Count | The total count of user-groups being returned across all pages. | 
| X-Page-Count | The count of pages which could be fetched with the criteria specified. | 
| X-Current-Page | The page being returned. |
| X-Page-Size | The number of entries in the page being returned. |
{:.bordertablestyle}

_please note that all of the above headers are strings_

#### __Examples__
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

#### __Schema Properties__

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
* __groups:__ _string[]_; The list of groups that the user is a current member of including user-groups and product configurations. See [Groups example](#getUserGroupsExample).
* __id:__ _string_
* __lastname:__ _string_
{% include apiRef/statusDescription.md %}
* __type:__ _string_, possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.html#identity) for more information.
* __username:__ _string_; The user's username (applicable for Enterprise and Federated users). For most Adobe ID users, this value will be the same as the email address.

#### __Schema Model__

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

{% include apiRef/badRequest.md %}

{% include apiRef/unauthorized.md %}

{% include apiRef/forbidden.md %}

{% include apiRef/notFound.md object="group" %}
