---
layout: default
nav_link: Samples
nav_level: 1
nav_order: 200
title: User Management Walkthrough
lang: en
---

# User Management Walkthrough

This walkthrough shows you how to set up the environment and make calls into the User Management API, using a JSON web token (JWT) to obtain authorization for your requests. The general technique applies to any Service Integrations with an Adobe API, and can be useful to anyone using the JWT workflow. 

The walkthrough integrates with a set of [Python samples]({{ site.github_url }}/tree/master/samples), available in GitHub, which demonstrate using the User Management API. Note that the sample scripts are intended to illustrate technique, and are not warranted for any purpose. 

A Postman collection is also available at the bottom of the page.

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

The **Retry-After** header is included in the 429 response and provides the minimum amount of time that the client should wait until retrying. See [RFC 7231](https://tools.ietf.org/html/rfc7231#section-7.1.3) for full information.

When making calls over the internet, other transient errors can occur so it is always a good practice to retry failed requests when certain HTTP status codes are returned.

The following function definition shows a technique for handling such errors that we call *exponential backoff*. If the Retry-After header is not found then we retry sending the request after a certain number of seconds, and increase that interval with each attempt.

```python
def make_call(self, path, body=None):
    if body:
        request_body = json.dumps(body)
        def call():
            return self.session.post(self.endpoint + path, auth=self.auth, data=request_body, timeout=self.timeout)
    else:
        def call():
            return self.session.get(self.endpoint + path, auth=self.auth, timeout=self.timeout)

    start_time = time()
    result = None
    for num_attempts in range(1, self.retry_max_attempts + 1):
        try:
            result = call()
            if result.status_code == 200:
                return result
            elif result.status_code in [429, 502, 503, 504]:
                if self.logger: self.logger.warning("UMAPI timeout...service unavailable (code %d on try %d)",result.status_code,num_attempts)
                retry_wait = 0
                if "Retry-After" in result.headers:
                    advice = result.headers["Retry-After"]
                    advised_time = parsedate_tz(advice)
                    if advised_time is not None:
                        # header contains date
                        retry_wait = int(mktime_tz(advised_time) - time())
                    else:
                        # header contains delta seconds
                        retry_wait = int(advice)
                if retry_wait <= 0:
                    # use exponential back-off with random delay
                    delay = randint(0, self.retry_random_delay)
                    retry_wait = (int(pow(2, num_attempts - 1)) * self.retry_first_delay) + delay
            elif 201 <= result.status_code < 400:
                raise ClientError("Unexpected HTTP Status {:d}: {}".format(result.status_code, result.text), result)
            elif 400 <= result.status_code < 500:
                raise RequestError(result)
            else:
                raise ServerError(result)
        except requests.Timeout:
            if self.logger: self.logger.warning("UMAPI connection timeout...(%d seconds on try %d)", self.timeout, num_attempts)
            retry_wait = 0
            result = None
        if num_attempts < self.retry_max_attempts:
            if retry_wait > 0:
                if self.logger: self.logger.warning("Next retry in %d seconds...", retry_wait)
                sleep(retry_wait)
            else:
                if self.logger: self.logger.warning("Immediate retry...")
    total_time = int(time() - start_time)
    if self.logger: self.logger.error("UMAPI timeout...giving up after %d attempts (%d seconds).", self.retry_max_attempts, total_time)
    raise UnavailableError(self.retry_max_attempts, total_time, result)
```
The above function definition is taken from the [Connection.py](https://github.com/adobe-apiplatform/umapi-client.py/blob/master/umapi_client/connection.py#L397) class inside [UMAPI-Client](https://github.com/adobe-apiplatform/umapi-client.py). 




## Postman collection for UMAPI samples  

### Environment configuration  

Download [this](UMAPI_SAMPLES.postman_collection.json) json file locally and import it to your Postman environment.  
Click Collections menu in Postman and select the `UMAPI SAMPLES` to view its Variables menu in the main page area.  
Fill in the `CURRENT VALUE` field the associated values obtained from your [developer portal](https://developer.adobe.com)'s integration/project (at least the first 5 rows)  
Before running any API in the list, you need to run first the `Auth - Obtain Access Token` to have an active token for this session.  


