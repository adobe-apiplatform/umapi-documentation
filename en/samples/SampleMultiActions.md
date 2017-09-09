---
layout: default
nav_link: Multi-Action Requests
nav_level: 2
nav_order: 270
lang: en
---

# Perform Multiple Actions for One User

This creates a user with an Enterprise ID, then performs a series of actions for that user. It adds the user to a product profile, adds two product entitlements for the user, and then removes one of the product entitlements.

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
      },
      {
        "add" : {
          "product" : [
            "PhotoshopCreative",
            "IllustratorCreative"
          ]
        }
      }
      {
        "remove" : {
          "product" : [
            "PremiereCreative"
          ]
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
