---
title: Product Information APIs
layout: default
nav_link: Product Information APIs
nav_order: 470
nav_level: 3
lang: en
---
# <a name="productInfoApis" class="api-ref-title">Product Information APIs</a>

**DEPRECATED:** These APIs have been deprecated. An exact date for removal will be confirmed before the end of 2017 but you should look to update your scripts as soon as possible.

<hr class="api-ref-rule">

Use the Product and Product Profile APIs to retrieve information about your organization's products.

Product access for individual users is controlled through membership in [user groups](glossary.md#usergroup) and [product profiles](glossary.md#productProfile). You cannot create these groups through the User Management API. Before you can manage product access for users, you must create and name user groups and product profiles using the [Admin Console](glossary.md#adminconsole).

A product can have more than one profile associated with it, to allow different access privileges for different sets of users. For example, if your organization uses Adobe Document Cloud Pro, you could have one product profile that blocks access to related services and another that only allows access to E-sign services.

## Query Products and Profiles
To get information about products and product profiles, use the following APIs:
* [Get a list of products](product.md)
* [Get a product profile](group.md)

## Manage User Access to Products
Both individual users and user groups can be members of a product profile. An individual user can gain access to a particular product directly, or through user-group membership. Within a product profile, member users can be assigned an admin role.

To manage product access for individual users, use the [Action API](ActionsRef.md).
* Use the _add_ and _remove_ actions on a _user_ to control membership in a specified _usergroup_ or _productConfiguration_ 
* Use the _addRole_ and _removeRole_ actions on a _user_ to control administrative rights in groups.
 
## Manage Product Admin Rights
See [Manage Entitlements](../RefOverview.md#provision)

<hr class="api-ref-rule">
