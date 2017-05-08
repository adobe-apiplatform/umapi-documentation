# Product Access and Role Management

Product access for individual users is controlled through membership in user groups and product configurations. You cannot create these groups through the User Management API. Before you can manage product access for users, you must create and name user groups and product configurations using the [Admin Console](https://adminconsole.adobe.com/enterprise/).

A product can have more than one license configuration associated with it, to allow different access privileges for different sets of users. For example, if your organization uses Adobe Document Cloud Pro, you could have one product configuration that blocks access to related services and another that only allows access to E-sign services.

Both individual users and user groups can be members of a product configuration. An individual user can gain access to a particular product directly, or through user-group membership. Within a product configuration, member users can be assigned an admin role.

You can manage access for individual users through the **action/{orgId}** endpoint. In addition, you can manage access rights through the individual endpoints for products and product configurations that are defined for your organization.

***

### Managing access through user actions

You can manage memberships and user roles for individual users or user groups in a POST request to the **action/{orgId}** resource. The JSON payload specifies actions to take for a **"user"** or a **"usergroup"**. There are two kinds of actions, those that control memberships, and those that control administrative roles within a group.

* [Membership Actions](#actions): You can add or remove membership in user groups and product configurations for a given **"user"**. You can modify the list of member users for a given **"usergroup"**, as well as the group's memberships in product configurations.
* [Role Management Actions](#adminrole): To change a user's administrative role within a product configuration, use **"addRoles"** or **"removeRoles"** actions for a given "user" and "product".

***

### **Managing access through product endpoints**

You can manage membership and administrative rights for specific products and product configurations in a POST request to the **.../{productId}/admins** or **.../{configId}** resource. The JSON payload specifies lists of users and user groups to add or remove. See full details below at [Manage Access through Product Endpoints](#productendpoints)

* You can obtain a list of product IDs defined for your organization with a call to the **product**resource for your organization.

```
GET [UM_Server]/{orgId}/products
```


For full reference details, see **[List and Query Products](queryproducts.md)**.
* You can obtain a list of product configuration IDs defined for a product with a call to the **configurations** resource for that product.

```
GET [UM_Server]/{orgId}/products/{productId}/configurations
```


For full reference details, see **[List and Query Product Configurations](queryproductconfigs.md)**.

***

## Membership Actions

Membership actions, like other user-management actions, are addressed in a POST request to the **actions/{orgId}** endpoint.

* [Per-user membership operations](#peruser)
* [Per-group membership operations](#pergroup)

### Per-user membership operations

You can add or remove memberships in the "do" list for a given "user". The **add** action adds the user to one or more product configurations or user groups. Similarly, the **remove** action removes membership for that user.

```json
[
  {
    "user" : "jdoe@myCompany.com",
    "do" : [{
        "add" : {
            "productConfiguration" : [ "Config1_Nickname", ... ],
            "usergroup" : [ "UserGroup1_Name", ... ]
         }
       },
       {
        "remove" : {
            "productConfiguration" : [ "Config2_Nickname" ],
            "usergroup" : [ "UserGroup12_Name" ]
         }
       }]
  }
]
```

You can remove a maximum of 10 memberships in one command entry, unless you use the special "all" parameter to remove all memberships for the user.

```json
[
  {
    "user" : "jdoe@myCompany.com",
       "do" : [ { "remove" : "all" } ]
    }
]
```

### Per-group membership operations

To update the membership lists for a given user group, specify **add** and **remove** actions in the "do" list for the "usergroup". You can add or remove member users, and also add and remove the user group's membership in specific product configurations.

You can remove a maximum of 10 memberships in one command entry, unless you use the special "all" parameter to remove all user or product configurations memberships for a user group.

```json
[
  {
    "usergroup" : "UserGroup1_Name",
    "do" : [{
        "add" : {
            "productConfiguration" : [ "Config1_Nickname", ... ],
            "users" : [ "user1@myCompany.com" , ... ]
       },
       {
        "remove" : {
            "productConfiguration" : [ "Config2_Nickname", ... ],
            "users" : [ "user2@myCompany.com" , ... ]
         }
       }]
  }
]
```

You can remove a maximum of 10 memberships in one command entry, unless you use the special "all" parameter to remove all users and memberships for the group.

```json
[
  {
    "usergroup" : "UserGroup1_Name",
       "do" : [ { "remove" : "all" } ]
    }
]
```

***

## Role Management Actions

You can add or remove a specific administrative role for a member user of a specific product or Product Configuration.

The **addRoles** action adds administrative access of a particular type for one or more products. For example, to add the Product Owner Admin role for a user:

```json
[
  {
    "user" : "jdoe@myCompany.com",
    "do" : [{
        "addRoles" : {
            "productAdmin" : ["Product1_Name"]
        }
      }]
  }
]
```

The **removeRoles admin** action removes the admin role for the user for a given product configuration.

```json
{ "removeRoles" : { "admin" : [ "Product1_Name" ] } }
```

***

## Manage Access through Product Endpoints

You can manage membership and administrative roles for products and product configurations by sending POST requests to the specific endpoint for specific products or configurations (rather than the **action** endpoint).

```json
POST [UM_Server]/{orgId}/product/{productId}/admin
POST [UM_Server]/{orgId}/products/{productId}/configurations/{configId}
```

**HEADERS** : You must include these headers in your request:

* **Authorization** : A current access token obtained from token-exchange request.
* **Content-type** : application/json
* **x-api-key** : The API key assigned to your API client account.

Note that **testOnly** query parameter is not supported for these endpoints.

**BODY** : The body of your request must contain the JSON-format **commands** list.

### Manage Product Admin Roles

In a POST request to a specific product's **/admin** resource, the JSON payload specifies lists of users whom to add or remove the admin role. You only need to specify the lists you are modifying.

```json
POST [UM_Server]/{orgId}/product/{productId}/admin

{
    "addProductAdmin" : [
        "jdoe@myCompany.com"
    ],
    "removeProductAdmin": [
        "ann.other@myCompany.com"
    ]
}
```

### Manage Product Configuration Memberships and Admin Roles

In a POST request to a specific product configuration resource, the JSON payload specifies lists of users and user groups to add or remove from membership, and users for whom to add or remove the admin role. You only need to specify the lists you are modifying.

```json
POST [UM_Server]/{orgId}/products/{productId}/configurations/{configId}

{
    "addUsers": [
        "a.smith@myCompany.com"
    ],
    "removeUsers": [
        "b.jones@myCompany.com"
    ],
    "addUserGroups": [
        "UMSDK User Group"
    ],
    "removeUserGroups": [
        "UMSDK User Group 2"
    ],
    "addAdminUsers" : [
        "jdoe@myCompany.com"
    ],
    "removeAdminUsers": [
        "ann.other@myCompany.com"
    ]
}
```
