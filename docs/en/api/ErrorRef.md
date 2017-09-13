---
layout: page
nav_link: Error Conditions
nav_order: 470
nav_level: 1
lang: en
---

# Error Conditions

The possible error codes and messages are listed with their context and descriptions.

* **error.user.not_found**
    * user or usergroup action command
    * An attempt to operate on a user or usergroup that does not exist.

* **error.user.not_in_org**
    * add/create, remove, update, removeFromOrg, resetPassword
    * An attempt to operate on a user who is not part of your organization or may be part of the organization but not owned by the organization. For example, updating a user who is in your organization but is owned by a different organization.

* **error.user.nonexistent**
    * add/create, remove, update, removeFromOrg, resetPassword
    * An attempt to operate on a user who does not exist.

* **error.user.nonexistent_or_has_conflicting_parameters**
    * add/create, remove, update, removeFromOrg, resetPassword
    * An attempt to operate on a user or usergroup that does not exist.

* **error.user.already_in_org**
    * add, create
    * The user specified already is a member of the organization.

* **error.user.already_invited**
    * add
    * The user specified already has an active invitation to your organization.

* **error.user.must_match_email**
    * add/create
    * The user name must be a valid email address and match the email field in the request. Some FederatedID organizations do not have this requirement.

* **error.user.type_must_not_be_adobeid**
    * update
    * The operation in the command cannot be applied to an Adobe ID.

* **error.user.type_unknown**
    * (internal) Type of user could not be determined.

* **error.user.not_found_or_ambiguous**
    * (internal) More than one user matches ID.

* **error.user.name.invalid**
    * add/create
    * Something about the user name is invalid, such as length or illegal character.

* **error.user.user_list.invalid**
    * add/remove membership
    * Something about a user name is invalid, such as length or illegal character.

* **error.user.type.missing**
    * (internal) Type of user could not be determined.

* **error.user.email.invalid**
    * The email address is invalid: more than 60 characters long, missing @, or contains illegal character.

* **error.user.belongs_to_another_org**
    * create, update
    * The specified user belongs to a different organization and cannot be accessed.

* **error.user.type_mismatch**
    * create
    * An attempt was made to add a Federated user to a Enterprise domain or the reverse.

* **error.user.change_domain_update.no**
    * update
    * An attempt was made to change a user email where the new email is in a different domain.

* **error.user.id_missing**
    * User ID is missing where required.

* **error.user.firstname_missing<br>error.user.lastname_missing**
    * User first or last name is missing where required.

* **error.user.name_in_use**
    * update
    * An attempt was made to change the user name but the new user name was already in use.

* **error.user.email.name_in_use**
    * update
    * An attempt was made to change the user email but the new email address was already in use by a different user.

* **error.user.name.contains.email**
    * add/create
    * An attempt to create a user with a username as email address in a Federated ID configured organization with SAML username setting.

* **error.user.update_failed**
    * update usergroup
    * An attempt to change usergroup membership failed.

* **error.user.already_exists**
    * A user to be added to a user group is already a member.

* **error.user.command.missing.arguments**
    * A usergroup command is missing required fields.

* **error.user.productadmin.group.not_found**
    * product admin operation
    * A user group being added/removed from a product is not found.

* **error.user.productadmin.add.user.failed**
    * add admin access to product
    * User access rights update failed.

* **error.user.productadmin.remove.admin.failed**
    * remove admin access to product
    * User access rights update failed.

* **error.command.add_remove.list**
    * add, remove
    * There must be a JSON object or "all" as the value for add or remove.

* **error.command.add_remove.duplicate.user_list**
    * add, remove
    * A user is listed twice in the list of users to add or remove.

* **error.command.add_remove.duplicate.product_list**
    * add, remove
    * There is more than one "product" key in the object for add or remove.

* **error.command.add_remove.duplicate.group_list**
    * add, remove
    * There is more than one "group" key in the object for add or remove.

* **error.command.add_remove.duplicate.usergroup_list**
    * add, remove usergroup
    * A User Group name is provided twice in the list of groups to add or remove.

* **error.command.add_remove.duplicate.productadmin_list**
    * add, remove productAdmin role for user in action command
    * The user appears twice in the list of product's admin users.

* **error.command.add_remove.invalid.usergroup_list**
    * add or remove groups for a product config
    * No user groups were found to add or remvove

* **error.command.product.not_found**
    * access or update product info or user lists for a product
    * The product was not found.

* **error.usergroup.already_exists**
    * add, remove usergroup
    * A User Group name is provided twice in the list of groups to add or remove.

* **error.command.add_remove.duplicate.user_list**
    * add, remove usergroup
    * A user name is provided twice in the list of users to add or remove for a usergroup.

* **error.command.add_remove.key.unknown**
    * add, remove
    * There is an unknown key (other than group or product) in the object for add or remove.

* **error.command.add_remove.user_usergroup.missing**
    * add, remove
    * No "user" or "usergroup" entry in the object for add or remove.

* **error.command.add_remove.missing_list**
    * add, remove
    * No product or group entry in the object for add or remove.

* **error.command.add_remove.list_too_long**
    * add, remove
    * Too many entries in the product or group list in add or remove, or too many steps in a command.

* **error.command.add_remove.list_not_array**
    * add, remove
    * List of products or groups in an add or remove must be a JSON array.

* **error.command.add_remove.group_or_product_name_too_long**
    * add, remove
    * Name of a group or product configuration is too long.

* **error.command.boolean_expected**
    * useAdobeID
    * Value of the flag must be true or false.

* **error.command.create.object_expected**
    * add, create
    * Value of the command must be a JSON object, "{...}"

* **error.command.create.string_expected**
    * option, email, country, firstname, lastname
    * Values of these items must be JSON strings.

* **error.command.create.more_than_one**
    * add, create
    * A command can contain only add or create step.

* **error.command.create.not_first**
    * add, create
    * An add or create step must the first one in a command.

* **error.command.create.key.unknown**
    * add, create
    * An unknown key was found in the JSON object for a create step

* **error.command.update.option.no**
    * option
    * The option value is allowed only in addAdobeID, createEnterpriseID, and createFederatedID. See also "error.option.illegal".

* **error.command.domain.missing**
    * domain
    * A domain element must be present when the user name is not an email address.

* **error.command.domain.must_be_used_with_nonemail_username**
    * domain
    * The domain value can only be used when the user field is not null and not an email address

* **error.domain.trust.nonexistent**
    * remove, update, removeFromOrg, removeFromDomain
    * Attempt to remove a user by trustee organization or user who does not own domain.

* **error.command.domain.string_expected**
    * domain
    * The domain value must be a JSON string.

* **error.command.string.too_long**
    * A user name, identifier, or domain name string is too long. Maximum is 250 characters.

* **error.command.string_expected**
    * requestId, user
    * The user name or requestId field is not a JSON string.

* **error.command.removefromorg.not_last**
    * removeFromOrg
    * This must be the last step in a command.

* **error.command.illegal_entry**
    * A command operation is not legal.

* **error.command.step.unknown**
    * A command operation is not legal.

* **error.command.object_not_empty**
    * removeFromOrg, resetPassword
    * The JSON object for these operations must be empty.

* **error.command.malformed**
    * The JSON in the request body has a syntax error, is not a JSON array, or is empty.

* **error.command.steps.malformed**
    * do
    * The value of do element must be a JSON array.

* **error.command.user.missing**
    * A user element must be present in each action/orgId command.

* **error.command.user_usergroup.missing**
    * Missing root command in action request
    * A user or usergroup element must be present in each action command.

* **error.usergroup.not_found**
    * add usergroup to config
    * A named User Group is not found.

* **error.usergroup.user_list.invalid**
    * add or delete users in group action command
    * The provided list of users did not change the group membership.

* **error.usergroup.update.failed**
    * add or delete usergroup action or add/remove usergroup for config
    * The user group was not updated.

* **error.usergroup.command.missing.arguments**
    * usergroup command action
    * No users or profiles found to associate with the user group.

* **error.country.invalid**
    * create
    * The country code is not legal or specifies a country in which Adobe does not do business

* **error.organization.invalid_id**
    * all
    * The organization ID in the URL is invalid or missing.

* **error.organization.invalid_name**
    * The organization name is null, illegal, or not found.

* **error.organization.migrating**
    * add/create, remove, update, removeFromOrg, resetPassword
    * Returned if the organization is in a migrating state. Changes cannot be made to an org when it is migrating. Part of EVIP workflows.

* **error.group.not_found**
    * /users, add, remove
    * A named group or product configuration was not found.

* **error.group.invalid_list**
    * add, remove
    * A list of groups or product configurations is empty or contains a null entry.

* **error.option.illegal**
    * The "option" flag value in a user add or create call (addAdobeID, createEnterpriseID, createFederatedID) is not one of the defined values.

* **error.api.not_available**
    * A referenced API is not currently available.

* **error.api.user.not.parent.org**
    * add/create, remove, removeFromOrg, removeFromDomain, update
    * Attempt to perform operations on a user by domain trustee organization.

* **error.resetpw.user_must_be_enterprise_type**
    * resetPassword
    * A user referenced in resetPassword is not an Enterprise ID. You cannot reset passwords for Adobe IDs or Federated IDs.

* **error.update.domain.mismatch**
    * update
    * The domain in the request does not match the domain of the user.

* **error.update.username.no**
    * update
    * The user name cannot be updated. However, changing the email changes the user login name.

* **error.update.country.no_update**
    * update
    * The country of a user cannot be updated.

* **error.apikey.invalid**
    * any request
    * Organization's API key in headers not valid

* **invites.pending.not_found**
    * any pending-invites request
    * No pending invites exist for the given email address or for the organization

* **invites.pending.resend.error**
    * request resend of pending invite
    * A server-side error occurred when resending pending invites

* **invites.pending.revoke.error**
    * request revocation of pending invite
    * A server-side error occurred when revoking pending invites

* **error.internal.create_failed**
    * create
    * Operation failed for unknown reason.

* **error.internal.update_failed**
    * update
    * Operation failed for unknown reason.

* **error.internal.removefromorg**
    * removeFromOrg
    * Operation failed for unknown reason.

* **error.internal.add**
    * add
    * Operation failed for unknown reason.

* **error.internal.group.remove**
    * group remove operation failed

* **error.internal.exceptionflys**
    * any
    * Unknown error occurred.

* **error.internal.notification.failed**
    * add, remove, removeFromOrg
    * Unknown error occurred trying to authorize a Digital Marketing Cloud product.

* **error.internal.notification.failed.jem**
    * add, remove, removeFromOrg
    * Unknown error occurred trying to update product use for Creative Cloud or Document Cloud products.

* **error.internal.notification.failed.dma**
    * add, remove, removeFromOrg
    * Unknown error occurred trying to update product use for Digital Marketing Cloud products.

* **error.internal.everybody_group.not_found**
    * add, create
    * A user could not be added to this root group, which should always exist.

* **error.internal.invite.email_template_misconfigured**
    * add, createEnterpriseID
    * The organization is misconfigured or an email template for an invitation could not be found.

* **error.internal.reset_password_email**
    * resetPassword
    * The reset password email send failed.

* **error.internal.no_email_for_user**
    * resetPassword
    * Unable to get email address for user to send reset password message. Try updating the email address for the user.

* **plc.not_found**
    * access or update to a config endpoint
    * The Product License Configuration was not found.

* **plc.admin.group.not_found**
    * access or update to admin user list at config endpoint
    * The admin user list for the Product License Config was not found.

* **plc.admin.already_added<br>plc.add.admin.error<br>plc.remove.admin.error**
    * add or remove admin user to config
    * The admin user already exists or doesn't exist in list

* **error.productadmin.add.user.failed<br>error.productadmin.remove.admin.failed**
    * update to admin user list for product
    * The admin user list was not updated.

* **FAILED_TO_ADD_TO_PLC<br>FAILED_TO_REMOVE_FROM_PLC**
    * add or remove user to config
    * Attempt to add or remove user failed

* **<a name="adobeidno" class="api-ref-subtitle">error.update.adobeid.no</a>**
    * update action workflows
    * The operation in the command cannot be applied to an Adobe ID.