# Adobe User Management SDK Samples

The following samples show the request format and JSON command structures for a variety of user-management tasks. We create a user of each type, update that user's information, and add and remove product profile memberships for the user. We show how to retrieve information about users and product profiles we have added, and how to remove a user from the organization. Additional examples show how to combine multiple actions for a single user, and perform actions for multiple users in one request.

For better readability, the samples show the unprocessed JSON array for each request body, and use placeholder values for enterprise-specific variables, which you should replace with your own values: {myDomain}, {myOrgId}, {myApiKey}, {myAccessToken}.

* [ExchangeJWT.py](#exchangejwtpy): Shows how to construct a JSON Web Token (JWT) and exchange it for an access token.
* [AddAdobeIDUser.py](#addadobeiduserpy): Adds an Adobe ID user.
* [CreateEnterpriseUser.py](#createenterpriseuserpy): Creates an Enterprise ID user.
* [CreateFederatedUser.py](#createfederateduserpy): Creates a Federated ID user.
* [UpdateUser.py](#updateuserpy): Updates a Federated user.
* [GroupInformation.py](#groupinformationpy): Retrieve information about user-groups and product profiles defined for your organization.
* [UserInformation.py](#userinformationpy): Retrieve information about users in for your organization.
* [UserInformationByGroup.py](#userinformationbygrouppy): Retrieve a list of users within a specified group.
* [RemoveFromOrg.py](#removefromorgpy): Remove a user from membership in your organization.
* [UserMultipleOperations.py](#usermultipleoperationspy): Create an Enterprise user and add them to a user-group and provision access to a product profile.

## ExchangeJWT.py

This Python script shows how to construct a JSON Web Token (JWT) and exchange it for an access token which can then be used to make User Management requests. You **must** create the JWT that encapsulates your *technical-account* credentials. You will then exchange this JWT for the API access token in the *access request*. The Python script shows how to create a JWT using the **pyjwt** library using the variables `org_id`, `tech_acct`, `ims_host`, `api_key` and `priv_key_filename` which are all defined in **usermanagement.config**.

Once this has been achieved you can use the token to obtain an access token for the User Management API. The second part of the script constructs a request that contains the JWT, and receives the access token in the response. Your **usermanagement.config** will be populated with the generated JWT ('jwt_token') and Access Token ('access_token').

## AddAdobeIDUser.py

This example shows how to add an independent Adobe ID using the [Action API]().

## CreateEnterpriseUser.py

This example shows how to add an Enterprise ID using the [Action API]().

## CreateFederatedUser.py

This example shows how to add a Federated ID using the [Action API](). You can create a user ID that includes the domain, or specify the domain separately from the user ID.

## UpdateUser.py

This example replaces the First Name and Last Name values for an existing user with the user's initials. All other user-information properties remain unchanged.

## GroupInformation.py

This sample shows how to retrieve information about user-groups and product profiles defined for your organization using the `GET /v2/usermanagement/groups/{orgId}/{page}` API. The 0 at the end of the URL, sets the page index to 0, causing the call to retrieve the first 200-entry page of groups.

## UserInformation.py

This sample shows how to retrieve information about users in for your organization using the `GET /v2/usermanagement/users/{orgId}/{page}` API. The 0 at the end of the URL, sets the page index to 0, causing the call to retrieve the first 200-entry page of users.

## UserInformationByGroup.py

This sample shows how to retrieve information about users within a specific group using the `GET /v2/usermanagement/users/{orgId}/{page}/{groupName}` API. `{groupName}` is the product profile's unique nickname you assign to it in the [Admin Console](https://adminconsole.adobe.com/enterprise)

## RemoveFromOrg.py

This sample shows how to remove a user from membership in your organization.

## UserMultipleOperations.py

It is more efficient to bundle actions for a user into a single request. You can use the User Management API to control product access by managing the membership of User Groups and Product Profiles that you have created and named in the [Admin Console](https://adminconsole.adobe.com/enterprise).

* To manage memberships for users and User Groups, use the **add** and **remove** actions for an individual **user** or **usergroup**.
* To manage product Admin roles for a _user_, use the **addRoles** and **removeRoles** actions for the individual **user** and **product** configuration.

See the Action API for further information on the different commands available. This sample bundles actions for a single user by creating an Enterprise ID and then adding them to a product profile and user-group.

## MultipleUsers.py

It is more efficient to bundle actions for many users into single requests, especially when multiple users are added to the same product profiles. This sample shows how to bundle actions for multiple users by creating two users with Enterprise IDs.

# Further Information 

Please refer to the [User Management SDK documentation]() for further information and guidance.
