---
layout: default
nav_link: Samples
nav_level: 1
nav_order: 200
title: User Management Walkthrough
lang: en
---

This walkthrough shows you how to set up the environment and make calls into the User Management API, using a JSON web token (JWT) to obtain authorization for your requests. The general technique applies to any Service Integrations with an Adobe API, and can be useful to anyone using the JWT workflow. 

The walkthrough integrates with a set of [Python samples]({{ site.github_url }}/tree/master/samples), available in GitHub, which demonstrate using the User Management API. Note that the sample scripts are intended to illustrate technique, and are not warranted for any purpose. 

| Sample | Description |
| :--- | :--------- |
| [ExchangeJWT.py]({{ site.github_url }}/blob/master/samples/JWTExchange.py) | Shows how to construct a JSON Web Token (JWT) and exchange it for an access token. |
| [AddAdobeIDUser.py]({{ site.github_url }}/blob/master/samples/AddAdobeIDUser.py) | Adds an Adobe ID user. |
| [CreateEnterpriseUser.py]({{ site.github_url }}/blob/master/samples/CreateEnterpriseUser.py) | Creates an Enterprise ID user. |
| [CreateFederatedUser.py]({{ site.github_url }}/blob/master/samples/CreateFederatedUser.py) | Creates a Federated ID user. |
| [UpdateUser.py]({{ site.github_url }}/blob/master/samples/UpdateUser.py) | Updates a Federated user. |
| [GroupInformation.py]({{ site.github_url }}/blob/master/samples/GroupInformation.py) | Retrieve information about user-groups and product profiles defined for your organization. |
| [UserInformation.py]({{ site.github_url }}/blob/master/samples/UserInformation.py) | Retrieve information about users in for your organization. |
| [UserInformationByGroup.py]({{ site.github_url }}/blob/master/samples/UserInformationByGroup.py) | Retrieve a list of users within a specified group. |
| [RemoveFromOrg.py]({{ site.github_url }}/blob/master/samples/RemoveFromOrg.py) | Remove a user from membership in your organization. |
| [UserMultipleOperations.py]({{ site.github_url }}/blob/master/samples/UserMultipleOperations.py) | Create an Enterprise user and add them to a user-group and provision access to a product profile. |
{:.bordertablestyle}  

***
## Using the Samples

* [Prerequisites](#prerequisites)
* [Setting up the Environment](#setting-up-the-environment)
* [Constructing User Management Requests](#constructing-user-management-requests)
    - [Constructing the Request](#constructing-the-request)
    - [Constructing a JSON command](#constructing-a-json-command)
    - [Making a request](#making-a-request)
* [Retrying Requests](#retrying-requests)

### Prerequisites

* Download [Python 3](https://www.python.org)
* 'Pip' is included as part of the download but it is recommended that you update it:
```
pip3 install --upgrade pip
```

All sample scripts use the Python packages `PyJWT`, `cryptography`, and `requests`. You must install these packages before running the scripts. You can install the packages with the following commands:
```
pip3 install pyjwt
pip3 install cryptography
pip3 install requests
```

### Setting Up the Environment

Our sample directory includes a sample **usermanagement.config**. To make all the scripts more readable and adaptable, we use variables defined in this separate configuration file. To produce and send requests, the file defines the following values which you must update before attempting to run any of the samples:
```
[server]
host = usermanagement.adobe.io
endpoint = /v2/usermanagement
ims_host = ims-na1.adobelogin.com
ims_endpoint_jwt = /ims/exchange/jwt

[enterprise]
domain = <my enterprise domain>
fed_domain = <my federated domain>
org_id = my organization id
api_key = my api key/client id
client_secret = my api client secret
tech_acct = my api client technical account
priv_key_filename = my private key filename
```

### Constructing User Management Requests

All of the samples have been simplified to demonstrate interacting with the User Management API. We construct a JSON body for the request, send the request and then output the response. We do not attempt to deal with failures, retries or managing request limits but this **must** be considered by our clients.

#### Constructing the Request

The first part of each script constructs a request using the variables that we defined to set the URL and headers.

```python
# method parameters
url = "https://" + host + endpoint + "/action/" + org_id
headers = {
    "Content-type" : "application/json",
    "Accept" : "application/json",
    "x-api-key" : api_key,
    "Authorization" : "Bearer " + access_token
    }
```

#### Constructing a JSON command

The body of the request contains the JSON command structure. First, we create the JSON array:

```python
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

```python
# prepare body
body = json.dumps(json_data)
```

#### Making a request

Finally, we connect to the server, send the request we have created, and receive a response:

```python
# send http request
res = requests.post(url, headers=headers, data=body)
```

This very simple call is an illustration of the basic technique. In a real application, you would make a more robust call that includes error handling and recovery. See [Retrying requests](#retrying-requests) below for details of handling the throttling limitations.

```python
# send request with retrying
send_request_retry("POST", url, headers, body)
```

Finally, to see the result of our request, we print the response.

```python
# print response
print(res.status_code)
print(res.headers)
print(res.text)
```


### Retrying requests

The server only accepts a certain number of requests per interval. If your own client exceeds this limit, you receive a response with the status code **429 (Too Many Requests)**. If the total of calls made by all clients exceeds the limit, you will also receive the response **429 (Too Many Requests)**.

When making calls over the internet, other transient errors can occur so it is always a good practice to retry failed requests when certain HTTP status codes are returned.

The following function definition shows a technique for handling such errors that we call *exponential backoff*. We retry sending the request after a certain number of seconds, and increase that interval with each attempt.

```python
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

