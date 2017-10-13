---
layout: default
nav_link: Get Groups and Profiles
nav_order: 420
nav_level: 2
lang: en
title: Get User Groups and Product Profiles
---

# <a class="api-ref-title" name="getGroups">Get User Groups and Product Profiles</a>

```
GET /v2/usermanagement/groups/{orgId}/{page}
```

Retrieves a paged list of all user groups and product profiles in your organization along with information about them. You can make multiple paginated calls to retrieve the full list of product profiles.

__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#throttle) for full details.

* [Parameters](#parameters)
* [Responses](#responses)
* [Request Examples](#exampleRequests)
* [Throttling Limits](#throttle)

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include_relative partials/orgIdDescription.md %} |
| X-Api-Key | header | true | {% include_relative partials/apiKeyDescription.md %} |
| page | path | true | The page number being requested. |
| Authorization | header | true | {% include_relative partials/authorizationDescription.md %} |
| content-type | header | false | {% include_relative partials/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include_relative partials/requestIdDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [200: OK](#200getGroupsWithPage)
- [400: Bad Request](#400getGroupsWithPage)
- [401: Unauthorized](#401getGroupsWithPage)
- [403: Forbidden](#403getGroupsWithPage)
- [429: Too Many Requests](#throttle)

### <a name="200getGroupsWithPage" class="api-ref-subtitle">__200 OK__</a>
A successful request returns a response body with the requested group data in JSON format. When the response contains the last paged entry, the response includes the field `lastPage : true`. If the returned page is not the last page, make additional paginated calls to retrieve the full list.


#### Example
<a name="getGroupsExample" class="api-ref-subtitle">Response returning three groups which is also the past page.</a>
```json
{
  "lastPage": true,
  "result": "success",
  "groups": [
        {
          "groupName": "Administrators",
          "memberCount": 11
        },
        {
          "groupName": "Document Cloud 1",
          "memberCount": 26
        },
        {
          "groupName": "Default Support Profile",
          "memberCount": 0
        }
    ]
}
```

<a name="getGroupsBeyondPageBoundaryExample" class="api-ref-subtitle">Request for page number beyond the page for which group data is available.</a>
```json
{
    "lastPage": true,
    "result": "Not found"
}
```

#### __Schema Properties__

* __groupName:__ _string_
* __memberCount:__ _integer_; The count of all members of the group.

#### __Schema Model__

```json
{
  "groupName": "string",
  "memberCount": integer
}
```

{% include_relative partials/badRequest.md anchor="400getGroupsWithPage" %}

{% include_relative partials/unauthorized.md anchor="401getGroupsWithPage" %}

{% include_relative partials/forbidden.md anchor="403getGroupsWithPage" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
Retrieve the first page of groups:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/groups/12345@AdobeOrg/0 \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```

Retrieve the fourth page of groups:
```
curl -X GET https://usermanagement.adobe.io/v2/usermanagement/groups/12345@AdobeOrg/4 \
  --header 'Authorization: Bearer ey...' \
  --header 'X-Api-Key: 88ce03094fe74f4d91c2538217d007fe'
```

## <a name="throttle" class="api-ref-subtitle">__Throttling__</a>

{% include_relative partials/throttling.md client=5 global=100 %}

