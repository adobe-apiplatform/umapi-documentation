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
| [get_oauth_token.py]({{ site.github_url }}/blob/master/samples/get_oauth_token.py) | Shows how to obtain an access token using OAuth Server-to-Server credentials. |
| [get_jwt_token.py]({{ site.github_url }}/blob/master/samples/get_jwt_token.py) | Shows how to obtain an access token using a locally constructed JWT and exchanging it for an access token. |
| [add_Adobe_ID.py]({{ site.github_url }}/blob/master/samples/add_Adobe_ID.py) | Creates an Adobe ID user. |
| [add_Enteprise_ID.py]({{ site.github_url }}/blob/master/samples/add_Enteprise_ID.py) | Creates an Enterprise ID user. |
| [add_federated_id.py]({{ site.github_url }}/blob/master/samples/add_federated_id.py) | Creates a Federated ID user. |
| [update_account.py]({{ site.github_url }}/blob/master/samples/update_account.py) | Updates an account's metadata. |
| [get_groups_and_profiles.py]({{ site.github_url }}/blob/master/samples/get_groups_and_profiles.py) | Retrieve information about user-groups and product profiles defined for your organization. |
| [get_users_in_org.py]({{ site.github_url }}/blob/master/samples/get_users_in_org.py) | Retrieve information about all accounts in for your organization. |
| [get_users_by_group.py]({{ site.github_url }}/blob/master/samples/get_users_by_group.py) | Retrieve members' list of a specified group. |
| [get_user_info.py]({{ site.github_url }}/blob/master/samples/get_user_info.py) | Retrieve details on the a specific account.|
| [remove_account.py]({{ site.github_url }}/blob/master/samples/RemoveFromOrg.py) | Soft or hard removal of an account from the Organization. |
| [multi_action.py]({{ site.github_url }}/blob/master/samples/UserMultipleOperations.py) | Demo multi action request |
| [source.csv]({{ site.github_url }}/blob/master/samples/UserMultipleOperations.py) | Sample csv file for the multi_action.py script. |
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
* 'pip' is included as part of the download but it is recommended that you update it:
```
pip install --upgrade pip
```
* create a vitual environment (optional)
```
python -m venv path/to/ENV
```
activate it:
```
source path/to/ENV/bin/activate
```
* install dependencies

All sample scripts use the Python packages `PyJWT`, `cryptography`, and `requests`. You must install these packages before running the scripts. You can install the packages with the following commands:
```
pip install requests
```
For DEPRECATED JWT workflows this modules need to be installed as well: _PyJWT_ and _cryptography_

### Setting Up the Environment

Each sample file contains some variables at the top that need to be initialised based on the information generated at Project creation phase, or specific to the action needed (like sample account info, or existing account's email):
```
ACCESS_TOKEN = ''
CLIENT_ID = ''
ORG_ID = ''
# add below an existing account's email from Admin Console
USER_EMAIL = ''
```


#### Constructing a Request

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

The body of the request is a list of JSON objects. You can add maximum 10 such objects in this list. Sample  for 

```python
body = \
[
  {
    "user" : "john.doe@domain.com",
    "do" : [
      {
        "addAdobeID" : {
          "email" : "john.doe@domain.com",
          "firstname": "John",
          "lastname": "Doe",
          "country": "US"
          "option": "ignoreIfAlreadyExists"
        }
      }
    ]
  }
]
```

#### Making a request

Finally, we connect to the server, send the request we have created, and receive a response:

```python
# send http request
r = requests.request(method, url, data=body, headers=headers)
```

This very simple call is an illustration of the basic technique. In a real application, you would make a more robust call that includes error handling and recovery.  
See [Retrying requests](#retrying-requests) below for details of handling the throttling limitations.
The main function in the sample will rely on the execution of the `make_call` function

```python
# send request with retrying
r = make_call(method, url, body)
```

All samples will use these default call management settings:
```
UMAPI_URL = <API specific url here>
MAX_RETRIES = 4
TIMEOUT = 120.0
RANDOM_MAX = 5
FIRST_DELAY = 3
```
Finally, for convenience and demo, we print to the screen output for body of the request, headers used and URL plus the result of the API response as a dict.

```python
if __name__ == '__main__':
    rez = add_adobe_id(MAIL,FIRST,LAST,COUNTRY)
    print(rez)
```


### Retrying requests

The server only accepts a certain number of requests per interval. If your own client exceeds this limit, you receive a response with the status code **429 (Too Many Requests)**. If the total of calls made by all clients exceeds the limit, you will also receive the response **429 (Too Many Requests)**.

The **Retry-After** header is included in the 429 response and provides the minimum amount of time that the client should wait until retrying. See [RFC 7231](https://tools.ietf.org/html/rfc7231#section-7.1.3) for full information.

When making calls over the internet, other transient errors can occur so it is always a good practice to retry failed requests when certain HTTP status codes are returned.

The following function definition shows a technique for handling such errors that we call *exponential backoff*. If the Retry-After header is not found then we retry sending the request after a certain number of seconds, and increase that interval with each attempt.

```python
def make_call(method, url, body={}):
    # call manager function with retry mechanism
    # returns the API response
    retry_wait = 0
    h = {'Accept' : 'application/json',
         'x-api-key' : CLIENT_ID,
         'Authorization' : 'Bearer ' + ACCESS_TOKEN}
    if body:
        h['Content-type']  = 'application/json'
        body = json.dumps(body)
        method = 'POST'
    for num_attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f'Calling {method} {url}\n{body}' )
            r = requests.request(method, url, data=body, headers=h, timeout=TIMEOUT)
            if r.status_code == 200:
                return json.loads(r.text)
            elif r.status_code in [429, 502, 503, 504]:
                print(f'UMAPI timeout... (code {r.status_code} on try {num_attempt})')
                if retry_wait <= 0:
                    delay = randint(0, RANDOM_MAX)
                    retry_wait = (pow(2, num_attempt - 1) * FIRST_DELAY) + delay
                if 'Retry-After' in r.headers.keys():
                    retry_wait = int(r.headers['Retry-After']) + 1
            else:
                print(f'Unexpected HTTP Status: {r.status_code}: {r.text}')
                return
        except Exception as e:
            print(f'Exception encountered:\n {e}')
            return
        if num_attempt < MAX_RETRIES:
            if retry_wait > 0:
                print(f'Next retry in {retry_wait} seconds...')
                sleep(retry_wait)
    print(f'UMAPI timeout... giving up after {MAX_RETRIES} attempts.')
```

## Postman collection for UMAPI samples  

### Environment configuration  

 Download [this](https://github.com/adobe-apiplatform/umapi-documentation/blob/master/docs/en/samples/UMAPI%20SAMPLES.postman_collection2.json) json file locally and import it to your Postman environment.  
 Click Collections menu in Postman and select the `UMAPI SAMPLES` to view its Variables menu in the main page area.  
 Fill in the `CURRENT VALUE` field with the associated values obtained from your [developer portal](https://developer.adobe.com)'s integration/project (at least the first 5 rows)  
 Before running any API in the list, you need to run `OAuth S2S - Obtain Access Token` or `JWT Auth - Obtain Access Token` first to have an active token generated for the session.  
 
