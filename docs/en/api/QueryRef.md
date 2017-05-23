---
layout: default
nav_link: User and Product Query Resource Reference
nav_order: 500
nav_level: 2
lang: en
---

# User and Product Query Resource Reference

You can query the Adobe database for users who are members of your oganization, and access information about user-groups, products, and product configurations that are defined for your organization. Membership in user groups and in product configurations controls a user's access to Adobe products in your organization.

* [Access User Information](#access-user-information)
* [Access User Group Information](#access-user-group-information)
* [Access Product Information](#access-product-information)
* [Access Product Configuration Information](#access-product-configuration-information)

***

### Notation

In syntax statements for endpoints, the following notation is used:

* **[UM_Server]** is the UM API server: **https://usermanagement.adobe.io/v2/usermanagement/**
* Curly braces indicate a variable, to be replaced with specific values for your organization.
  - Replace **{orgId}** with your organization's unique ID, which looks like this: "12345@AdobeOrg".
  - Replace **{...Id}** or **{...Name}** elements with the unique ID or name assigned to user groups, products, and product configurations that are defined for you organization.
  - Replace the **{page}** element with the zero-based index for the first requested page of the paged result.
  - Replace the **{email}** element with the email address of a user in your organization.

### Request headers

You must include these headers in all requests:

* **Authorization** : A current access token obtained from login request.
* **x-api-key** : The API key for your organization, obtained from the Developer Portal.

***

### Paginated Lists

All calls to resources that provide lists are paginated. A zero-based page index is either an optional query parameter,or is included in the endpoint URL. For example:

```
GET [UM_Server]/{orgId}/usergroups[?page={n}]
GET [UM_Server]/{orgId}/users/{page}/{groupName}
```

In either case, the **page** parameter is a 0-based page index for the starting entry of the returned list. The number of entries returned in each call can vary, but never exceeds the maximum of 200 entries. Where optional, default is 0.

When a page contains the last entry, the response includes the field "lastPage : true". If the returned page is not the last page, make additional paginated calls to retrieve the full list.

***

## Access User Information

The full list of users in your organization is available through the **{orgId}/users/** resource. You can also get member lists through the user-group and product-configuration resources.

When you add a user to your organization, they receive an email invite, and are not included in the user list until they respond. You can access the list of these pending users through the **{orgId}/invites/** resource.

* Get a paged list of all users for your organization:

```
GET [UM_Server]/{orgId}/users
```
* Retrieve information for a specific user using their email address, which serves as the UID:

```
GET [UM_Server]/{orgId}/users/{email}
```
* Get a paged list of all users who have been invited to join your organization but have not yet responded:

```
GET [UM_Server]/{orgId}/invites
```
* Retrieve information for a specific pending user:

```
GET [UM_Server]/{orgId}/invites/{email}
```

NOTE: For compatability with previous releases, existing user information can also be accessed through the **users/{orgId}** or **organizations/{orgId}/users** resources.

```
GET [UM_Server]/users/{orgId}/{page}
GET [UM_Server]/organizations/{orgId}/users
GET [UM_Server]/organizations/{orgId}/users/{email:.*}
```

For full reference details, see **[List and Query Users](queryusers.md)**.

***

## Access User Group Information

User group information defined through the [Admin Console](https://adminconsole.adobe.com/enterprise/) is available through either **{orgId}/users-groups** resource.

* List a page of user-groups defined for your organization.

```
GET [UM_Server]/{orgId}/user-groups
```
* Retrieve information for a specific user group.

```
GET [UM_Server]/{orgId}/user-groups/{groupId}
```
* List a page of users who belong to a specific user group.

```
GET [UM_Server]/{orgId}/user-groups/{groupId}/users
```
* List a page of users with admin role for a specific user group.

```
GET [UM_Server]/{orgId}/user-groups/{groupId}/admins
```

NOTE: For compatability with previous releases, user-group information can also be accessed through the **groups/{orgId}** resource.

```
GET [UM_Server]/groups/{orgId}
GET [UM_Server]/groups/{orgId}/{groupId}
```

For full reference details, see **[List and Query User Groups](queryusergroups.md)**.

***

## Access Product Information

Product information defined for your organization in the [Admin Console](https://adminconsole.adobe.com/enterprise/) is available through the **{orgId}/products/** resource. You can list products and examine information for individual products.

* List a page of products for your organization.

```
GET [UM_Server]/{orgId}/products
```
* Retrieve information for a specific product.

```
GET [UM_Server]/{orgId}/products/{productId}
```

For full reference details, see **[List and Query Products](queryproducts.md)**.

* NOTE: Send a **POST** request to a product endpoint to manage user access rights for that product. For syntax details, see **[Manage Product Access Rights](accessActionsRef.md)**.

***

## Access Product Configuration Information

Products are associated with product configurations that are defined in the [Admin Console](https://adminconsole.adobe.com/enterprise/). For a given product, you can list and examine the associated product configurations.

All products and product configurations can be accessed through endpoints under the **{orgId}/products** resource.

* List a page of product configurations defined for your organization, or for a specific product.

```
GET [UM_Server]/{orgId}/products/{productId}/configurations
```
* Retrieve information about a specific product configuration.

```
GET [UM_Server]/{orgId}/products/{productId}/
        configurations/{configId}
```
* List a page of users who belong to a specific product configuration.

```
GET [UM_Server]/{orgId}/products/{productId}/
        configurations/{configId}/users
```
* List a page of users with admin role for a specific product configuration.

```
GET [UM_Server]/{orgId}/products/{productId}/
          configurations/{configId}/admins
```

NOTE: For compatibility with previous releases, product configuration information can also be accessed through the **groups/{orgId}** resource.

```
GET [UM_Server]/groups/{orgId}/{page}
```

For full reference details, see **[List and Query Product Configurations](QueryProductConfigs.md)**.

* Send a **POST** request to a product-configuration endpoint to manage the access rights of members. For syntax details, see **[Manage Product Access Rights](accessactionsref.md)**.
