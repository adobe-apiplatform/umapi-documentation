# User Management Walkthrough

This walkthrough goes through sample Python scripts that demonstrate how to construct and send a request for an access token, and then use it to construct and send a user-management request and receive the response. Individual samples show the format of requests for representative user-management actions.

## Sections

* [Setting Up the Environment](#setup)
* [Constructing a JSON Web Token](#jwt)
* [Constructing an Access Request](#access)
* [Constructing User-Management Requests](#manage)
* [Retrying Requests](#retry)

## Using the sample scripts

The sample scripts are intended to illustrate technique, and are not warranted for any purpose.

The sample scripts use the Python packages **PyJWT**, **cryptography**, and **requests**. You must install these packages before running the scripts. You can install the packages with the following commands:

```json
pip install pyjwt
pip install cryptography
pip install requests
```

***

## Setting Up the Environment

The main Python script shows how to construct a JWT, exchange it for an access token and make user management requests. To make the script more readable and adaptable, we use variables defined in a separate configuration file named **usermanagement.config**. To produce and send the requests, the file defines these values:

```json
[server]
host = usermanagement.adobe.io
endpoint = /v2/usermanagement
ims_host = ims-na1.adobelogin.com
ims_endpoint_jwt = /ims/exchange/jwt

[enterprise]
domain = my domain
org_id = my organization id
api_key = my api key/client id
client_secret = my api client secret
tech_acct = my api client technical account
priv_key_filename = my private key filename
```

In the main script, we first import all the required libraries:

```json
import sys
if sys.version_info[0] == 2:
    from ConfigParser import RawConfigParser
    from urllib import urlencode
if sys.version_info[0] >= 3:
    from configparser import RawConfigParser
    from urllib.parse import urlencode
import time
import jwt
import requests
import json
import email.utils
import math
import random
```

The next part reads the configuration file and sets up the required variables.

```json
# read configuration file
config = RawConfigParser()
config.read("usermanagement.config")

# server parameters
host = config.get("server", "host")
endpoint = config.get("server", "endpoint")
ims_host = config.get("server", "ims_host")
ims_endpoint_jwt = config.get("server", "ims_endpoint_jwt")

# enterprise parameters used to construct JWT
domain = config.get("enterprise", "domain")
org_id = config.get("enterprise", "org_id")
api_key = config.get("enterprise", "api_key")
client_secret = config.get("enterprise", "client_secret")
tech_acct = config.get("enterprise", "tech_acct")
priv_key_filename = config.get("enterprise", "priv_key_filename")
```

***

## Constructing a JSON Web Token

You must create the JWT that encapsulates your technical-account credentials. You will exchange this JWT for the API access token in the access request. The following Python script shows how to create a JWT for a sample enterprise using the **pyjwt** library and the variables we have defined for the required components of the JWT.

Set the expiration time for the JWT to one day from the current time. This is a typical and recommended validity period.

```json
# set expiry time for JSON Web Token
expiry_time = int(time.time()) + 60*60*24
```

Use the enterprise credentials and expiration value to create the JWT payload.

```json
# create payload
payload = {
    "exp" : expiry_time,
    "iss" : org_id,
    "sub" : tech_acct,
    "aud" : "https://" + ims_host + "/c/" + api_key,
    "https://" + ims_host + "/s/" + "ent_user_sdk" : True
}
```

Get the private key we will use to sign the JWT.

```json
# read private key from file
priv_key_file = open(priv_key_filename)
priv_key = priv_key_file.read()
priv_key_file.close()
```

Create the JWT, signing it with the private key.

```json
# create JSON Web Token
jwt_token = jwt.encode(payload, priv_key, algorithm='RS256')
# decode bytes into string
jwt_token = jwt_token.decode("utf-8")
```

For debugging purposes, we print the result. In practice, you should never print or retain JWTs that you create.

```json
# print JSON Web Token
print("Your JSON Web Token is:")
print(jwt_token)
```

***

## Constructing an Access Request

To obtain an access token for the User Management API, this part of the script constructs a request that contains the JSON Web Token (JWT), and receives the access token in the response. First, we set variables for request URL and headers.

```json
# method parameters
url = "https://" + ims_host + ims_endpoint_jwt
headers = {
    "Content-Type" : "application/x-www-form-urlencoded",
    "Cache-Control" : "no-cache"
}
```

The credentials are placed in the body of the POST request. Notice that the "client_id" value is your API key.

```json
body_credentials = {
    "client_id" : api_key,
    "client_secret" : client_secret,
    "jwt_token" : jwt_token
}
body = urlencode(body_credentials)
```

Finally, we connect to the server, send the request, and receive the response.

```json
# send http request
res = requests.post(url, headers=headers, data=body)
```

If the request is successful, we extract the access token from the body of the response. For this demonstration, we print the result.

```json
# evaluate response
if res.status_code == 200:

    # extract token
    access_token = json.loads(res.text)["access_token"]

    # print access token
    print("Your access token is:")
    print(access_token)

else:

    # print response
    print(res.status_code)
    print(res.headers)
    print(res.text)
```

***

## Constructing User Management Requests

Each of the sample requests is produced by a Python script that constructs the JSON body of the request, sends the request, and receives the response. The first part of each script constructs a request using the variables that we defined to set the URL and headers.

```json
# method parameters
url = "https://" + host + endpoint + "/action/" + org_id
headers = {
    "Content-type" : "application/json",
    "Accept" : "application/json",
    "x-api-key" : api_key,
    "Authorization" : "Bearer " + access_token
    }
```

### Constructing a JSON command

The body of the request contains the JSON command structure. First, we create the JSON array:

```json
json_data = \
[
  {
    "user" : "john.doe@" + domain,
    "do" : [
      {
        "addAdobeID" : {
          "email" : "john.doe@" + domain
        }
      }
    ]
  }
]
```

Next, we convert the JSON array to a string to be included in the request body:

```json
# prepare body
body = json.dumps(json_data)
```

### Making a request

Finally, we connect to the server, send the request we have created, and receive a response:

```json
# send http request
res = requests.post(url, headers=headers, data=body)
```

This very simple call is an illustration of the basic technique. In a real application, you would make a more robust call that includes error handling and recovery. The sample provides a retry function to handle the case where calls fail because you have sent too many in too short a time. See [Retrying requests](#retry) below for the function definition. To use this technique, make the request by calling this function:

```json
# send request with retrying
send_request_retry("POST", url, headers, body)
```

Finally, to see the result of our request, we print the response.

```json
# print response
print(res.status_code)
print(res.headers)
print(res.text)
```

***

## Retrying requests

The server only accepts a certain number of requests per interval. If your own client exceeds this limit, you receive a response with the status code **429 (Too Many Requests)**. If the total of calls made by all clients exceeds the limit,you receive a response with the status code **503 (Service Unavailable)**.

When making calls over the internet, other transient errors can occur so it is always a good practice to retry failed requests when certain HTTP status codes are returned.

The following function definition shows a technique for handling such errors that we call "exponential backoff". We retry sending the request after a certain number of seconds, and increase that interval with each attempt.

```json
def send_request_retry(method, url, headers, body):

    # initialize exponential backoff mechanism
    num_attempts = 0
    num_attempts_max = 4
    backoff_exponential_factor = 15 # seconds
    backoff_random_delay_max = 5 # seconds

    # try sending the request
    while True:

        # increase number of attempts
        num_attempts += 1

        # send request
        print("Sending request...")
        if method == "GET":
            res = requests.get(url, headers=headers)
        elif method == "POST":
            res = requests.post(url, headers=headers, data=body)
        else:
            res = None
            break

        # print response
        print(res.status_code)
        print(res.headers)
        print(res.text)

        # evaluate response
        if res.status_code in [ 429, 502, 503, 504 ]:

            # check number of attempts
            if num_attempts >= num_attempts_max:
                print("Aborting after " + str(num_attempts) + " failed attempts")
                break

            # set backoff time
            if "Retry-After" in res.headers:
                # parse Retry-After header
                retry_after_date = email.utils.parsedate_tz(res.headers["Retry-After"])
                if retry_after_date != None:
                    # header contains date
                    time_backoff = int(email.utils.mktime_tz(retry_after_date) - time.time())
                else:
                    # header contains delta seconds
                    time_backoff = int(res.headers["Retry-After"])
            else:
                # use exponential backoff with random delay
                time_backoff = int(math.pow(2, num_attempts-1)) * \
                    backoff_exponential_factor + \
                    random.randint(0, backoff_random_delay_max)

            # delay next request
            print("Retrying in " + str(time_backoff) + " seconds...")
            time.sleep(time_backoff)

        else:

            # stop sending request
            break

    # return response
    return res
```

***

## Sample Requests

The following samples show the request format and JSON command structures for a variety of user-management tasks. We create a user of each type, update that user's information, and add and remove product configuration memberships for the user. We show how to retrieve information about users and product configurations we have added, and how to remove a user from the organization. Additional examples show how to combine multiple actions for a single user, and perform actions for multiple users in one request.

For better readability, the samples show the unprocessed JSON array for each request body, and use placeholder values for enterprise-specific variables, which you would replace in your own scripts: {myDomain}, {myOrgId}, {myApiKey}, {myAccessToken}

* [Create users](samplecreate.md)
* [Update user information](sampleupdate.md)
* [Add and remove product access for a user](samplegroups.md)
* [Query user and product configuration information](samplequery.md)
* [Remove users](sampleremove.md)
* [Perform multiple actions for one user](samplemultiaction.md)
* [Perform actions for multiple users](samplemultiuser.md)
