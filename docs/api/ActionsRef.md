# User Management Actions

The body of a user-management request must contain a **commands** list, a JSON structure that specifies users to act upon, and the actions to take.

## Command structure

The JSON **commands** structure contains an array of individual command entries, where each command names a user and applies a series of actions on that user. Each requested action is a step in the command. For each step, information relevant to the requested action is included in the step. For details of the syntax for each action, see [Action data formats](#action-data-formats).

```json
[ {"user" : "uid1@domain",
   "do" : [ { "action" : {action_params} },
            {... }
           ] },
   {"user" : "uid2@domain",
    "do" : [ {"action" : {...} , ...] } ,
    ...
 ]
```

In the "user" field, the user specification is usually an email address with a UID and domain component. Your organization can be configured to accept user IDs that are not email addresses. In either case, you can also specify a separate email address as a data field for the user.

In the case of Federated IDs that are not email addresses, you must supply the domain the user belongs to in order to create the user, and to perform update, add, remove, and removeFromOrg operations. To do this, add a "domain" field at the same level as the "user" field. For example:

```json
[ {"user" : "jdoe",
   "domain" : "example.com",
   "requestID" : "ed2149",
   "do" :  [ { "createFederatedID": {
             "email": "john.doe@myDomain",
             "country": "US",
             "firstname": "John",
             "lastname": "Doe"
             }
           },
         { "add" : { "productConfiguration" : [ "Photoshop", "Illustrator"] }
       }
      ]
   }
]
```

The "domain" field is ignored if the user has an Adobe ID or Enterprise ID.

### Identifying commands for debugging

In addition to the required "user" and "do" fields, a command can include a "requestID" field. The value is an arbitrary string that helps you identify a command if it is returned in an error response. For example, if you generate commands from a particular data structure in your program, you can use a requestID to tag those commands. You can then connect any errors back to your internal structure using the requestID value as an index.

Add the "requestID" field at the same level as the "user" field. For example:

```json
[ {"user" : "jdoe@example.com",
   "requestID" : "ed2146",
   "do" :  [{ "add" : { "product" : [ "Photoshop", "Illustrator"] } } ]
  },
    ...
 ]
```

### Command limits

The following limits apply to the "commands" structure and components:

| Component | Maximum |
| --- | --- |
| Size of JSON structure | 1 MB |
| Number of commands in the JSON structure per call | 10 |
| Number of action steps per command | 10 |
| Number of product configurations or products per command | 10 |

***

## Action data formats

The "do" element of a command specifies a set of action steps to perform on a user record. The following sections describe the specific action values and their parameters.

* [Create and add user operations](#create-and-add-user-operations)
* [User update operations](#user-update-operations)
* [Product access operations](#product-access-operations)
* [Remove user operations](#remove-user-operations)
* [Reset password operations](#reset-password-operations)

***

## Create and add user operations

There can be only one add or create user operation in a command and it must be the first step. The following actions create new user accounts in your organization:<br>

**createEnterpriseID<br>createFederatedID**

The **addAdobeID** action sends an email to a user with an existing Adobe ID, inviting them to join your organization. The invited user is not available for other operations, such as product access management, until they have accepted the invitation. When you add an Adobe ID user, the command must not include further steps for that user.

The parameters for a create or add user operation must include the user ID, and can include any other user-information fields. The fields that can be present depend on the ID type.

<caption> **User ID Fields**</caption>

| Field | Value | ID Type |
| --- | --- | --- |
| **email** | A valid email address. Limited to 64 characters. | Required for all types. |
| **firstname**, **lastname** | Maximum 250 characters | Not used for **addAdobeID**. Optional for **createEnterpriseID**and **createFederatedID**. |
| **country** | A valid ISO 2-character country code for a country in which Adobe does business. | Not used for **addAdobeID**. Optional for **createEnterpriseID**. Required for **createFederatedID**. |

In addition to the new user's field values, the parameters can include an "option" flag that specifies how to perform the create operation when a user with the given ID already exist in the user database:

* **"option" : "ignoreIfAlreadyExists"**
If the ID already exists, ignore the create step. Process any other steps in the command entry for this user.
* **"option" : "updateIfAlreadyExists"**
If the ID already exists, perform an Update action using the parameters in the create step. After updating all fields present in the step, process any other steps in the command entry for this user.

***

## Update user operations

The **update** action writes new personal information to the user's account details. You can only update Enterprise and Federated IDs that are managed by your enterprise.

* Independent Adobe IDs are managed by the individual user and cannot be updated through the User Management API. Attempting to update information for a user who has an Adobe ID is an error.
* For Federated IDs, the update request can only change the information that is stored by Adobe. You cannot change information your organization stores outside of Adobe through the User Management API. You can, however, include a "username" field for users whose email address is in your domain. The "username" value must not include an at-sign character (@).

The parameters of an **update** step specify the changed fields and their new values. If you do not specify a field, its value remains unchanged.

```json
[ {"user" : "jdoe@example.com",
   "do" : [ { "update" : {"email" : "jdoe@example.com",
           "firstname" : "Jane",
           "lastname" : "Doe",
           "username" : "jdoe"
        }
      }
    ]
  }
]
```

_NOTE: Currently, the country value cannot be updated after it is set._

***

## Product access operations

You can use the User Management API to manage product access for users by adding them to and removing them from your defined product configurations. These product configurations correspond to specific product access rights, so adding product access for a user is the same as adding that user to the corresponding product configuration.

When a user is a member of a product configuration, you can use action commands to grant and revoke administrative privilege for that user in that product configuration.

You cannot create product configurations through the User Management API. Before you can manage product access for users, you must create named product configurations for the products your organization uses, using the [Admin Console](https://adminconsole.adobe.com/enterprise/).

A product can have more than one configuration associated with it, to allow different access privileges for different sets of users. When you create a product configuration, you must assign it a unique, identifying name. For example, if your organization uses Adobe Document Cloud Pro, you could have one product configuration that blocks access to related services and another that only allows access to E-sign services. Assign unique names, such as "DC no services" and "DC e-sign". You can then use the "add" and "delete" actions to manage the membership of each product configuration.


_NOTE: If you have not yet upgraded your enterprise to support granular admin roles, you cannot create product configurations in the [Admin Console](https://adminconsole.adobe.com/enterprise/). Instead, you must add product access to user groups, and manage group membership to add and remove product access for users._

### Add product access

The **add productConfiguration** action adds the user to one or more product configurations, thereby adding a specific type of product access for the user.

```json
{ "add" : { "productFConfiguration" : [ "product_config_name", ...] } }
```

You can make a maximum of 10 individual product configuration additions in one command entry.

### Remove product access

The **remove** action removes the user from a product configuration, thereby removing a specific type of product access for the user.

```json
{ "remove" : { "productConfiguration" : [ "product_config_name", ...] } }
{ "remove" : "all" }
```

The special argument "all" removes the user from all product configurations, thereby removing all product access for the user.

You can remove a maximum of 10 product configuration removals in one command entry, unless you use the special "all" parameter to remove the user from all existing product configurations.

### Add admin role for products

The **addRoles admin** action adds the user to the list of admins for one or more product configurations.

```json
{ "addRoles" : { "admin" : [ "product_config_name", ...] } }
```

### Remove admin role for product configurations

The **removeRoles admin** action removes the admin role for the user for one or more product configurations.

```json
{ "removeRoles" : { "admin" : [ "product_config_name", ...] } }
```

## Remove user operations

These commands remove a user from membership in an organization, or from membership in a trusted domain of an organization.

There can only be a single **removeFromOrg** or **removeFromDomain** action in a command entry. If present, the removal action must be last step in the command entry.

* The **removeFromOrg** action removes the user from membership in the organization, and optionally from membership in a domain that is linked to the given organization through the trusted-domain relationship.

  - If the account is owned by the organization, the account is also deleted.
  - If the "removedDomain" argument is supplied, the user is also removed from that domain.
  - Note that Adobe IDs are never deleted because they are owned by the user, not the organization.



```json
{ "removeFromOrg" : { "removedDomain" : "domain_name"} }
```
* The **removeFromDomain** action removes the user from membership in your organization and from membership in a domain that is linked to the given organization through the trusted-domain relationship. Note that this results in the removal of provisioning for that user that is granted through any linked organization, not just the one specified in this call.

```json

 { "removeFromDomain" :
    { "removedDomain" : "domain_name" }
 }
```

***

## Reset password operations

For Enterprise IDs only, **resetPassword** action initiates the password-reset process for the user. The system sends a password-reset email to the user, and prevents login to the account until the password is reset.

```json
{ "resetPassword" : {} }
```
