---
layout: default
nav_link: Update User Information
nav_level: 2
nav_order: 230
lang: en
---

# Update User Information

This example replaces the First Name and Last Name values for an existing user with the user's initials. All other user-information properties remain unchanged.

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgID}
-------------------------- body ----------------------------
[
  {
    "user" : "john.doe@myDomain",
    "do" : [
      {
        "update" : {
          "firstname" : "J",
          "lastname" : "D"
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
