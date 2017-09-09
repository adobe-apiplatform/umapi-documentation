---
title: Delete User Group
layout: default
nav_link: Delete User Group
nav_order: 445
nav_level: 3
lang: en
---

# <a name="deleteUserGroup" class="api-ref-title">Delete User Group</a>
```
DELETE /v2/usermanagement/{orgId}/user-groups/{groupId}
```

* [Overview](#intro)
* [Parameters](#parameters)
* [Responses](#responses)
* [Example Requests](#exampleRequests)
* [Throttling Limits](#throttle)

<a name="intro" class="api-ref-subtitle"></a>
Permanently delete a [user-group](glossary.html#user-group) identified by the `groupId` from the given organization. When you remove a user-group, the users in that group are still retained in the Admin Console. However, if you have assigned product profiles to this group, then the users in the group will no longer have access to the associated products.

__Throttle Limits__: Maximum 5 requests per minute per a client. See [Throttling Limits](#throttle) for full details.

## <a name="parameters" class="api-ref-subtitle">Parameters</a>

This table summarizes the parameters and how they are provided:

| Name | Type | Required | Description |
| :--- | :------ | :---: | :------ |
| orgId | path | true | {% include apiRef/orgIdDescription.md %} |
| groupId | path | true | The id of the user-group. |
| x-api-key | header | true | {% include apiRef/apiKeyDescription.md %} |
| Authorization | header | true | {% include apiRef/authorizationDescription.md %} |
| Content-type | header | false | {% include apiRef/contentTypeDescription.md %} |
| X-Request-Id | header | false | {% include apiRef/requestIdDescription.md %} |
{:.bordertablestyle}

## <a name="responses" class="api-ref-subtitle">Responses</a>

__Content-Type:__ _application/json_

- [204: No Content](#204deleteUserGroup)
- [400: Bad Request](#400deleteUserGroup)
- [401: Unauthorized](#401deleteUserGroup)
- [403: Forbidden](#403deleteUserGroup)
- [429: Too Many Requests](#throttle)

### <a name="204deleteUserGroup" class="api-ref-subtitle">204 No Content</a>
The user-group has been successfully deleted and no longer exists.  

{% include apiRef/badRequest.md anchor="400deleteUserGroup" %}

{% include apiRef/unauthorized.md anchor="401deleteUserGroup" %}

{% include apiRef/forbidden.md anchor="403deleteUserGroup" %}

## <a name="exampleRequests" class="api-ref-subtitle">Example Requests</a>
```
 curl -ivs -X DELETE \
   http://usermanagement.adobe.io/v2/usermanagement/28E1E2EB570F90057F000101@AdobeOrg/user-groups/49371437 \
   -H 'authorization: Bearer {ACCESS_TOKEN}' \
   -H 'content-type: application/json' \
   -H 'x-request-id: user-assigned-request-id'
```


## <a name="throttle" class="api-ref-subtitle">Throttling</a>

{% include apiRef/throttling.md client=5 global=50 %}