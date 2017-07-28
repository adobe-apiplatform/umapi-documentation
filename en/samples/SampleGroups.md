---
layout: default
nav_link: Manage Product Access
nav_level: 2
nav_order: 250
lang: en
---

# Add and Remove Product Access

You can use the User Management API to control product access by managing the membership of User Groups and Product Configurations that you have created and named in the [Admin Console](https://adminconsole.adobe.com/enterprise/).

* To manage [memberships](#user-membership-actions) for users and User Groups, use the **add** and **remove** actions for an individual **user** or **usergroup**.
* To manage product [Admin roles](#manage-admin-roles) for a _user_, use the **addRoles** and **removeRoles** actions for the individual **user** and **product** configuration.
* To manage product Admin roles for a _product_, use the **addProductAdmin** and **removeProductAdmin** actions in a POST request to the product-specific endpoint.
* To manage [both membership and Admin roles for Product Configurations](#manage-membership-and-roles-for-a-product-configuration), send a POST request to the configuration-specific endpoint.

***

## Manage user memberships in User Groups and Product Configurations

You can manage memberships in an action for a "user" or in an action for a "usergroup".

### User membership actions

In the "do" list for a "user", add that user to membership in a User Group and two Product Configurations.

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgId}
-------------------------- body ----------------------------
[
  {
    "user" : "john.doe@myDomain",
    "do" : [
      {
        "add" : {
          "usergroup" : [
            "Marketing Reports & Analytics" ],
          "product" : [
            "MarketingCreative",
            "CreativeCloudComplete"
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

### User Group membership actions

In the "do" list for a "usergroup", add the User Group as a member of two Product Configurations, and add a user as a member of the User Group. This gives the new group member access to the products.

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgId}
-------------------------- body ----------------------------
[
  {
    "usergroup" : "Marketing Reports & Analytics",
    "do" : [
      {
        "add" : {
           "product" : [
            "MarketingCreative",
            "CreativeCloudComplete"
          ],
           "user" : [ "ann.other@myCompany.com" ]
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

Remove memberships for a User Group

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgId}
-------------------------- body ----------------------------
[
  {
    "usergroup" : "Marketing Reports & Analytics",
    "do" : [
      {
        "remove" : {
          "product" : [
            "CreativeCloudComplete"
          ],
           "user" : [ "ann.other@myCompany.com" ]
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

***

## Manage Admin Roles

You can manage which users have the Admin role for products with a POST request to either the **action/{orgId}** endpoint or to the specific product endpoint, **{orgId}/products/{productId}**

You can also manage the user membership and roles for Product Configurations with a POST request to the specific configuration endpoint, **{orgId}/products/{productId}/configurations/{configId}**.

### Manage roles for a user

Add and remove the Admin role for a specific user in specific Product Configurations with a POST request to the **action/{orgId}** endpoint.

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgId}
-------------------------- body ----------------------------
[
  {
    "user" : "john.doe@myDomain",
    "do" : [
      {
        "addRoles" : {
          "productAdmin" : [
            "MarketingCreative1",
            "CreativeCloudComplete"
          ]
        }
      }
      {
        "removeRoles" : {
          "productAdmin" : [
            "MarketingCreative2"
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

### Manage roles for member users of a product

Add and remove users to the Admin role for a specific product with a POST request to the product endpoint.

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/{myOrgId}/products/{myProductId}
-------------------------- body ----------------------------
[
  {
    "addProductAdmin" : [
        "jdoe@myCompany.com"
    ],
   "removeProductAdmin": [
        "ann.other@myCompany.com"
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

## Manage Membership and Roles for a Product Configuration

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/{myOrgId}/products/{myProductId}/configurations/{myConfigId}
-------------------------- body ----------------------------
[
  {
    "addUsers": [
        "ann.other@myCompany.com"
        ],
    "removeUsers": [
        "jdoe@myCompany.com"
        ],
    "addUserGroups": [
        "UMSDK User Group"
        ],
    "removeUserGroups": [
        "UMSDK User Group 2"
        ],
    "addAdminUsers" : [
        "ann.other@myCompany.com"
        ],
    "removeAdminUsers": [
        "adam.bede@myCompany.com"
        ]
    }
]
------------------------- headers --------------------------
Accept: application/json
Content-Type: application/json
x-api-key: {myApiKey}
Authorization: Bearer {myAccessToken}
```
