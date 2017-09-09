---
title: Get Users in Organization
layout: default
nav_link: /users/{orgId}/{page}
nav_order: 434
nav_level: 4
lang: en
---

# <a name="getUsersWithPage" class="api-ref-title">Get Users in Organization</a>

```
GET /v2/usermanagement/users/{orgId}/{page}
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#getUsersWithPageThrottle)

<a name="intro" class="api-ref-subtitle"></a>
Retrieve a paged list of all users in your organization along with information about them. The number of users returned in each call is subject to change but never exceeds 200 entries. You can make multiple paginated calls to retrieve the full list of users. The `domain` query parameter filters the results to only return users within a specified domain.  

__Throttle Limits__: Maximum 25 requests per minute per a client. See [Throttling Limits](#getUsersWithPageThrottle) for full details.

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| X-Api-Key | header | true | {% include apiRef/apiKeyDescription.md %} |
| page | path | true | The page number being requested. Page numbers greater than what exist will return the last page of users. |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
| domain | query | false | Retrieves users from a domain linked to an organization through the Trusted Domain relationship. |
| directOnly | query | false | {% include apiRef/directOnlyDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200getUsersWithPage)
- [400: Bad Request](#400getUsersWithPage)
- [401: Unauthorized](#401getUsersWithPage)
- [403: Forbidden](#403getUsersWithPage)
- [429: Too Many Requests](#getUsersWithPageThrottle)

### <a name="200getUsersWithPage" class="api-ref-subtitle">200 OK</a>
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

__users:__  
Represents a list of _User_ objects. Properties that are not populated __will not__ be returned in the response. Some properties are not applicable for particular account types.

* **adminRoles:** _string[]_; The list of groups or roles that the user holds an administrative role. See [AdminRoles](#getUserAdminRolesExample) for an example of the response. {% include apiRef/rolesDescription.md %}
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

{% include apiRef/badRequest.md anchor="400getUsersWithPage" %}

{% include apiRef/unauthorized.md anchor="401getUsersWithPage" %}

{% include apiRef/forbidden.md anchor="403getUsersWithPage" %}

{% include apiRef/notFound.md object="domain" anchor="404getUsersWithPage" %}


## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
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

## <a name="getUsersWithPageThrottle" class="api-ref-subtitle">Throttling</a>

{% include apiRef/throttling.md client=25 global=100 %}
