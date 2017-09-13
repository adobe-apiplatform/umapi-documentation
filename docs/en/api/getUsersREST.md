---
title: Get Users in Organization
layout: default
nav_link: /{orgId}/users
nav_order: 435
nav_level: 4
lang: en
---

# <a name="getUsersWithPage" class="api-ref-title">Get Users in Organization</a>

```
GET /v2/usermanagement/{orgId}/users
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#getUsersRESTThrottle)

<a name="intro" class="api-ref-subtitle"></a>
Retrieve a paged list of all users in your organization along with information about them. The number of users returned in each call is subject to change but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list of users.  

__Throttle Limits__: Maximum 25 requests per minute per a client. See [Throttling Limits](#getUsersRESTThrottle) for full details.

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Req? | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| X-Api-Key | header | true | {% include apiRef/apiKeyDescription.md %} |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| page | query | false | The page number being requested. Page numbers greater than what exist will return the last page of users. |
| content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
| directOnly | query | false | {% include apiRef/directOnlyDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200getUsersREST)
- [400: Bad Request](#400getUsersREST)
- [401: Unauthorized](#401getUsersREST)
- [403: Forbidden](#403getUsersREST)
- [429: Too Many Requests](#getUsersRESTThrottle)

### <a name="200getUsersREST" class="api-ref-subtitle">200 OK</a>
The response body contains a list of users in JSON format including the email, firstName and lastName. Please note that fields can be missing if there are no values, i.e. if the user is not a member of any groups then `groups` will not be returned. Use the response headers `X-Total-Count` and `X-Page-Count` to determine total number of users and total page count.

#### Headers

{% include apiRef/pagedResponseHeaders.md object="users" %}

#### Examples
<a name="getUsersRESTExample" class="api-ref-subtitle">Response returning three users with different group membership and administrative rights:</a>
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

#### Schema Properties

__user:__  
Represents a _User_ object. Properties that are not populated __will not__ be returned in the response. Some properties are not applicable for particular account types. See [Identity Types](glossary.html#identity) for more information on account types.

* **adminRoles:** _string[]_; The list of groups or roles that the user holds an administrative role. {% include apiRef/rolesDescription.md %}
* __countryCode:__ _string_; A valid ISO 2-character country code.
* __domain:__ _string_; The user's domain.
* __email:__ _string_
* __firstName:__ _string_
* __groups:__ _string[]_; The list of groups that the user is a current member of including user-groups and product profiles.
* __id:__ _string_
* __lastName:__ _string_
* __phoneNumber:__ _string_
{% include apiRef/statusDescription.md %}
* __userType:__ _string_, possible values: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`; The user type. See [Identity Types](glossary.html#identity) for more information.
* __username:__ _string_; The user's username (applicable for [Enterprise](glossary.html#enterpriseId) and [Federated](glossary.html#federatedId) users). For most [AdobeID](glossary.html#adobeId) users, this value will be the same as the email address.

#### Schema Model

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

{% include apiRef/badRequest.md anchor="400getUsersREST" %}

{% include apiRef/unauthorized.md anchor="401getUsersREST" %}

{% include apiRef/forbidden.md anchor="403getUsersREST" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
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

## <a name="getUsersRESTThrottle" class="api-ref-subtitle">Throttling</a>

{% include apiRef/throttling.md client=25 global=100 %}