---
layout: default
nav_link: Query User and Product Configuration
nav_level: 2
nav_order: 240
---

# Query User and Product Configuration Information

These samples show how to use GET requests to retrieve information about users and product configurations that are defined for your organization. In API requests and responses, a product configuration is identified by the unique nickname you assign to it in the [Admin Console](https://adminconsole.adobe.com/enterprise/). The 0 at the end of each URL sets the page index to 0, causing the call to retrieve the first 200-entry page of users.

## Request user information

This request retrieves the first 200-entry page. Repeat the request with page values 1, 2, 3, and so on, until the JSON result in the response contains the **lastPage** flag.

```json
========================= REQUEST ==========================
GET https://usermanagement.adobe.io/v2/usermanagement/users/{myOrgId}/0
------------------------- headers --------------------------
Accept: application/json
Content-Type: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```

## Request information for users in a Trusted Domain

This request retrieves the first 200-entry page. Repeat the request with page values 1, 2, 3, and so on, until the JSON result in the response contains the **lastPage** flag.

```json
========================= REQUEST ==========================

GET https://usermanagement.adobe.io/v2/usermanagement/users/{myOrgId}/0?domain=myDomain.com
------------------------- headers --------------------------
Accept: application/json
Content-Type: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```

## Request a list of product configurations defined for your organization.

```json
========================= REQUEST ==========================
GET https://usermanagement.adobe.io/v2/usermanagement/groups/{myOrgId}/0
------------------------- headers --------------------------
Accept: application/json
Content-Type: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```

## Request information for users belonging to a specific product configuration

```json
========================= REQUEST ==========================
GET https://usermanagement.adobe.io/v2/usermanagement/users/{myOrgId}/0/{myProductConfigName}
------------------------- headers --------------------------
Accept: application/json
Content-Type: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```
