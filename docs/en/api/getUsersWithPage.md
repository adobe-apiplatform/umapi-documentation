---
title: Get Users in Organization
layout: default
nav_link: Get Users in Organization
nav_order: 412
nav_level: 3
lang: en
---

# <a name="getUsersWithPage" class="api-ref-title">Get Users in Organization</a>

```
GET /v2/usermanagement/users/{orgId}/{page}
```

Retrieve a paged list of all users in your organization along with information about them. The number of users returned in each call is subject to change, currently the limit is max 2000 entries/page. You can make multiple paginated calls to retrieve the full list of users. The `domain` query parameter filters the results to only return users within a specified domain.

__Throttle Limits__: Maximum 25 requests per minute per a client. See [Throttling Limits](#getUsersWithPageThrottle) for full details.

* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#getUsersWithPageThrottle)

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include_relative partials/orgIdDescription.md %} |
| X-Api-Key | header | true | {% include_relative partials/apiKeyDescription.md %} |
| page | path | true | The 0-based index of the page number being requested. If greater than last page number, returns the last page of users. The page size is variable with the current value returned in the X-Page-Size response header. |
| Authorization | header | true | {% include_relative partials/authorizationDescription.md %} |
| content-type | header | false | {% include_relative partials/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include_relative partials/requestIdDescription.md %} |
| domain | query | false | Retrieves users from a domain linked to an organization through the Trusted Domain relationship. |
| directOnly | query | false | {% include_relative partials/directOnlyDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200getUsersWithPage)
- [400: Bad Request](#400getUsersWithPage)
- [401: Unauthorized](#401getUsersWithPage)
- [403: Forbidden](#403getUsersWithPage)
- [429: Too Many Requests](#getUsersWithPageThrottle)

:warning: Use only those properties that are documented in the [Response Properties](#ResponseProps) section. Additional fields can appear in the response, but should not be relied upon.

### <a name="200getUsersWithPage" class="api-ref-subtitle">200 OK</a>

A successful request returns a response body with the requested user data in JSON format. When the response contains the last paged entry, the response includes the field `lastPage : true`. If the returned page is not the last page, make additional paginated calls to retrieve the full list.

[Identity Types](glossary.md#identity) explains the different account types available.

### Headers 

{% include_relative partials/pagedResponseHeaders.md object="users" %}

### Examples 

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
                "Marketing Cloud 1",
                "Marketing Cloud 2",
                "Creative Cloud 1",
                "Document Cloud 1",
                "_admin_Document Cloud 1",
                "_admin_Support for AEM Mobile",
                "_admin_Default Support configuration",
                "_admin_Creative Cloud 1"
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
                "Support for AEM Mobile",
                "_admin_Document Cloud 1",
                "_admin_Support for AEM Mobile",
                "_admin_Default Support configuration",
                "_admin_Creative Cloud 1",
                "_deployment_admin",
                "_developer_Document Cloud 1"
            ],
            "username": "joe",
            "domain": "example.com",
            "firstname": "First",
            "lastname": "Last",
            "country": "US",
            "type": "federatedID"
        }
    ]
}
```
<a name="getUsersExampleLastPage" class="api-ref-subtitle">Response that is the last page:
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

{% include_relative partials/badRequest.md anchor="400getUsersWithPage" %}

{% include_relative partials/unauthorized.md anchor="401getUsersWithPage" %}

{% include_relative partials/forbidden.md anchor="403getUsersWithPage" %}

{% include_relative partials/notFound.md object="domain" anchor="404getUsersWithPage" %}


## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
Retrieve the first page of users:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/0 \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
Retrieve the fifth page of users:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/4 \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
Retrieve the first page of users with domain _my-domain.com_:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/0?domain=my-domain.com \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```
Retrieve the first page of users including details of all the memberships (direct and indirect) for each user:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/users/12345@AdobeOrg/0?directOnly=false \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```

## <a name="getUsersWithPageThrottle" class="api-ref-subtitle">Throttling Limits</a>

{% include_relative partials/throttling.md client=25 global=100 %}
