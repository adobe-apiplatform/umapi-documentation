* __country:__ _string_; A valid ISO 2-character country code.
* __domain:__ _string_; The user's domain.
* __email:__ _string_; The user's email address.
* __firstname:__ _string_; The user's first name.
* __groups:__ _string[]_; The list of groups in which the user is a current member, including, user groups, product profiles, product admin groups, and group-specific admin groups. Administrative groups are named with a prefix and the group name. For example, `_product_admin_Photoshop`, `_admin_DesignTools`, or `_developer_Marketing`. You should avoid any logic that expects fixed group names as these are liable to change without notice. Organization-wide admin groups are:
  * `_org_admin`: The user is a [System Administrator](glossary.md#orgAdmin).
  * `_deployment_admin`: The user is a [Deployment Administrator](glossary.md#deployment).
  * `_support_admin`: The user is a [Support Administator](glossary.md#supportAdmin).
* __id:__ _string_; The user's unique identifier.
* __lastname:__ _string_; The user's last name.
* __status:__ _string_; A user's status with the organization. Only "active" users are returned by [Get User Information](getUser.html) and [Get Users in Organization](getUsersWithPage.html). One of the following: 
  * "active": Normal status for a user account in good standing.
  * "disabled": Disabled temporarily - user is not allowed to login, but is not removed.
  * "locked": Disabled permanently - user is not allowed to login, but is not removed.
  * "removed": The user account is being removed. 
* __type:__ _string_, The user type, one of: `{ "adobeID", "enterpriseID", "federatedID", "unknown" }`. See [Identity Types](glossary.md#identity) for more information.
* __username:__ _string_; The user's username (applicable for [Enterprise](glossary.md#enterpriseId) and [Federated](glossary.md#federatedId) users). For most [Adobe ID](glossary.md#adobeId) users, this value is the same as the email address.
* __tags:__ _string[]_; Returns a list of the tags applied to a user e.g. `["edu_student", "edu_staff"]`. This will not be returned if the user has no tags.
* **adminRoles:** _string[]_; Deprecated. Administrative roles are reflected in group memberships, returned in the `groups` field.