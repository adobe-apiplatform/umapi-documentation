---
layout: default
nav_link: Remove User
nav_level: 2
nav_order: 260
lang: en
---

# Remove a User from your Organization

The following examples show how to remove a user from membership in your organization, and from membership in a Trusted Domain.

## Remove user from membership in your organization

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
  }
]
------------------------- headers --------------------------
Accept: application/json
Content-Type: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```

***

## Remove user from membership in your organization and in a Trusted Domain

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgId}
-------------------------- body ----------------------------

[
   {
      "user" : "john.doe@myDomain",
      "do" : [
         { "removeFromOrg" :
            { "removedDomain" : "myDomain" }
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

***

## Remove user from membership in a Trusted Domain

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgId}
-------------------------- body ----------------------------

[
   {
      "user" : "john.doe@myDomain",
      "do" : [ { "removeFromDomain" :
                  { "domain" : "myDomain" }
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
