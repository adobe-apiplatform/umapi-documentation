---
layout: default
nav_link: List All Configurations for Organization
nav_order: 453
nav_level: 3
lang: en
---

# List All Configurations for Organization

```
GET /v2/usermanagement/groups/{orgId}/{page}
```

<a name="intro" class="api-ref-subtitle"></a>
This API retrieves a paged list of all product profiles in your organization along with information about them. You can make multiple paginated calls to retrieve the full list of product profiles.

__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#getUsersWithPageThrottle) for full details.

## __Parameters__

| Name | Type | Req? | Description |
| :--- | :------ | :--- | :--- | --- |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| X-Api-Key | header | true | {% include apiRef/apiKeyDescription.md %} |
| page | path | true | The page number being requested. |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
{:.bordertablestyle}


## __Responses__

- [200: OK](#200getGroupsWithPage)
- [400: Bad Request](#400getGroupsWithPage)
- [401: Unauthorized](#401getGroupsWithPage)
- [403: Forbidden](#403getGroupsWithPage)
- [429: Too Many Requests](#getGroupsWithPageThrottle)

### __Example Requests__
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

## <a name="getUsersWithPageThrottle" class="api-ref-subtitle">__Throttling__</a>

{% include apiRef/throttling.md client=5 global=100 %}


## __Responses__

__Content-Type:__ _application/json_

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
          "groupName": "Default Support configuration",
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

{% include apiRef/badRequest.md anchor="400getGroupsWithPage" %}

{% include apiRef/unauthorized.md anchor="401getGroupsWithPage" %}

{% include apiRef/forbidden.md anchor="403getGroupsWithPage" %}