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

Retrieves a paged list of all user groups and product profiles in your organization along with information about them. You can make multiple paginated calls to retrieve the full list.

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
| page | path | true | The 0-based index of the page number being requested. If greater than last page number, returns the last page of groups. |
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

:warning: Use only those properties that are documented in the [Response Properties](#ResponseProps) section. Additional fields can appear in the response, but should not be relied upon.

### <a name="200getGroupsWithPage" class="api-ref-subtitle">__200 OK__</a>
A successful request returns a response body with the requested group data in JSON format. When the response contains the last paged entry, the response includes the field `lastPage : true`. If the returned page is not the last page, make additional paginated calls to retrieve the full list.


### Examples 
<a name="getGroupsExample" class="api-ref-subtitle">Response returning three groups, which is also the last page.</a>
```json
{
  "lastPage": true,
  "result": "success",
  "groups": [
        {
          "type": "SYSADMIN_GROUP",
          "groupName": "Administrators",
          "memberCount": 11
        },
        {
          "type": "USER_GROUP",
          "groupName": "Document Cloud 1",
          "memberCount": 26,
          "adminGroupName": "_admin_Document Cloud 1",
          "licenseQuota": "2"
        },
        {
          "type": "PRODUCT_PROFILE",
          "groupName": "Default Support Profile",
          "memberCount": 0,
          "productName": "All Apps plan - 100 GB",
          "licenseQuota": "8"
        },
        {
          "type": "PRODUCT_ADMIN_GROUP",
          "groupName": "_product_admin_Adobe Document Cloud for business",
          "memberCount": 2,
          "productProfileName": "Adobe Document Cloud for business",
        },
        {
          "type": "DEVELOPER_GROUP",
          "groupName": "_developer_Adobe Document Cloud for business",
          "memberCount": 5,
          "productProfileName": "Adobe Document Cloud for business",
        }
    ]
}
```

<a name="getGroupsBeyondPageBoundaryExample" class="api-ref-subtitle">Response to request for an out-of-bounds page number.</a>
```json
{
    "lastPage": true,
    "result": "Not found"
}
```

## Response Properties 

A group entry can represent a product profile, a user group, or an administrative group. Different fields are returned for the different types of group. The `type` field identifies the group type:

* __type:__ _string_; The group type. One of:
  * USER_GROUP
  * PRODUCT_PROFILE
  * SYSADMIN_GROUP
  * DEPLOYMENT_ADMIN_GROUP
  * SUPPORT_ADMIN_GROUP
  * PRODUCT_ADMIN_GROUP
  * PROFILE_ADMIN_GROUP
  * USER_ADMIN_GROUP
  * DEVELOPER_GROUP
 
The following fields are present for all group types: 

* __memberCount:__ _integer_; The count of all members of the group.
* __adminGroupName__ _string_; The name of the group that lists the administrators for this user group or product profile. Field absent if there are no administrators for this user group or product profile. The name is in the format `_admin_user-group-name` or `_admin_product-profile-name`.
* __groupName:__ _string_; The name of the group (assigned in the Admin Console). There are three administrative groups with fixed names:
  * Administrators: `_org_admin` 
  * Support Administrators: `_support_admin` 
  * Deployment Administrators: `_deployment_admin` 

  In addition, there are administrative groups for each user group and product profile. There are also developer groups for product profiles.
  These are named with a prefix and the group name. For example,
  `_admin_Marketing Group`, `_product_admin_Adobe Document Cloud for business` or `_developer_Marketing Group`.
* __groupId:__ _long_; The unique identifier for the group.

The following field is returned for groups of type `USER_ADMIN_GROUP`:

* __userGroupName__ _string_; The name of the user group for which this group grants admin rights. 

The following field is returned for groups of type `PROFILE_ADMIN_GROUP`:

* __productProfileName__ _string_; The name of the product profile for which this group grants admin rights. 

The following fields are returned for groups of type `PRODUCT_PROFILE`:

* __productName__ _string_; The name of the product associated with this product profile. 
* __licenseQuota:__ _string_; The number of user licenses or the amount of resources alloted to this product profile.
 
### __Schema Model__

```json
{
  "type": "string",
  "memberCount": 0,
  "adminGroupName": "string",
  "groupName": "string",
  "userGroupName": "string",
  "productProfileName": "string",
  "productName": "string",
  "licenseQuota": "string",
  "groupId": long
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

