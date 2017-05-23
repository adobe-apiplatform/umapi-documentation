# Create Users

The following samples show how to create each type of user; an independent Adobe ID, an Enterprise ID, and a Federated ID.

## Create a User with an Adobe ID

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgID}
-------------------------- body ----------------------------
[
  {
    "user" : "john.doe@myDomain",
    "do" : [
      {
        "addAdobeID" : {
          "email" : "john.doe@myDomain"
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

## Create a User with an Enterprise ID

```json
========================= REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgID}
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

## Create a User with a Federated ID

You can create a user ID that includes the domain, or specify the domain separately from the user ID.

```json
========================== REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgID}
--------------------------body ----------------------------
[
  {
    "user" : "jdoe@myDomain.com ",
    "do" : [ { "createFederatedID" :
               {"email" : "john.doe@myDomain",
                "country" : "US",
                "firstname" : "John",
                "lastname" : "Doe" }
              }]
   }
]
```

```json
======================== REQUEST ==========================
POST https://usermanagement.adobe.io/v2/usermanagement/action/{myOrgID}
-------------------------- body ----------------------------
[
  {
    "user" : "jdoe",
    "domain" : "myDomain.com"
    "do" : [
      {
        "createFederatedID" : {
          "email" : "john.doe@myDomain",
          "country" : "US",
          "firstname" : "John",
          "lastname" : "Doe"
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
