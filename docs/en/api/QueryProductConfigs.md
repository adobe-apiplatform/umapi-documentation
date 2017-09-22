---
layout: default
nav_link: Product Profile APIs
nav_order: 450
nav_level: 3
lang: en
---

# Product Profile APIs

Use the product profile APIs to retrieve and update information about product profiles that are defined for your organization. Product profiles are defined in the [Admin Console](https://adminconsole.adobe.com/enterprise/). Membership in user groups and in product profiles controls a user's access to Adobe products in your organization.

Product profiles are listed under individual products; see [Product Information APIs](product.md).

* [Access Product Profile Information](#accessProductProfileInformation)
* [Update Product Profile Information](#updateProfileInfo)

## <a name="accessProductProfileInformation" class="api-ref-subtitle">Access Product Profile Information</a>

* Retrieve a paged list of all profiles that are defined for your organization.  
[Get All Profiles for Organization](getAllProfilesForOrg.md)

* For a given product, you can list and examine the associated product profiles.  
[Get Product Profiles](getProductProfile.md)
 
* Get a paged list of users who belong to a specific product profile.  
[Get Product Profile Users](getProductProfileUsers.md)
 
* Get a paged list of users with admin role for a specific product profile.  
[Get Product Profile Admin Users](getProductProfileUsers.md#adminUsers)

## <a name="updateProfileInfo" class="api-ref-subtitle">Update Product Profile Information</a>

To manage membership and administrative rights for a specific product profile, send a POST request to a product profile endpoint.  
[Update Product Profile Information](updateProductProfile.md)

