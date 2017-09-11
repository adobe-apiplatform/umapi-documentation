---
layout: default
nav_link: Multi-User Requests
nav_level: 2
nav_order: 280
lang: en
---

# Perform Actions for Multiple Users

It is more efficient to bundle actions for many users into single requests, especially when multiple users are added to the same product profiles. These samples show how to bundle actions for multiple users by creating two users with Enterprise IDs, and then, in another call, removing both users from the organization.

## Create two users

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgId}
-------------------------- body ----------------------------
[
  {
    "user" : "john.doe@myDomain",
    "do" : [
      {
        "createEnterpriseID" : {
          "email" : "john.doe@myDomain",
          "country" : "US",
          "firstname" : "John",
          "lastname" : "Doe"
        }
      }
    ]
  },
  {
    "user" : "jane.doe@myDomain",
    "do" : [
      {
        "createEnterpriseID" : {
          "email" : "jane.doe@myDomain",
          "country" : "US",
          "firstname" : "Jane",
          "lastname" : "Doe"
        }
      }
    ]
  }
]
------------------------- headers --------------------------
Accept: application/json
Content-Type: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```

## Remove two users

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgId}
-------------------------- body ----------------------------
[
  {
    "user" : "john.doe@myDomain",
    "do" : [
      {
        "removeFromOrg" : {}
      }
    ]
  },
  {
    "user" : "jane.doe@myDomain",
    "do" : [
      {
        "removeFromOrg" : {}
      }
    ]
  }
]
------------------------- headers --------------------------
Accept: application/json
Content-Type: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```
