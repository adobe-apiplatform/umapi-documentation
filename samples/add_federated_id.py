# Copyright (c) 2023 Adobe Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy of this 
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify, 
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or 
# substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.

# https://adobe-apiplatform.github.io/umapi-documentation/en/api/ActionsCmds.html
# POST /v2/usermanagement/action/{orgId}

import uuid

import json
import requests

# obtained via JWT or OAuth S2S workflow
ACCESS_TOKEN = ''
CLIENT_ID = ''
ORG_ID = ''
# for SSO where NameID is an attribute value of email format
UPN,EMAIL,FIRST,LAST,COUNTRY=('email@domain.com',
                              'email@domain.com',
                              'first_name',
                              'lastname',
                              'US')
# # for SSO where NameID is an attribute value of NON-email format, uncomment below
# UPN,EMAIL,FIRST,LAST,COUNTRY=('some-username',
#                               'email@domain.com',
#                               'first_name',
#                               'lastname',
#                               'US')                   
# simulate call or make changes in Admin Console:
IS_TEST = 'true'
# default call management settings
UMAPI_URL = 'https://usermanagement.adobe.io/v2/usermanagement/action/'
MAX_RETRIES = 4
TIMEOUT = 120.0
RANDOM_MAX = 5
FIRST_DELAY = 3


def add_federated_id(sso_username, email, first, last, country):
    url = UMAPI_URL + ORG_ID + '?testOnly=' + IS_TEST
    method = 'POST'
    body = format_select(sso_username, email, first, last, country)
    print(f'{body}')
    r = make_call(method, url, body)
    return r

def format_select(sso_username, email, first, last, country):
    # helper function to build the body of the create POST call
    domain = email[email.index('@') + 1:]
    j_format = {0: [{'user': sso_username,
                     'requestID': str(uuid.uuid1()),
                     'do': [{'createFederatedID': {
                                'email': email,
                                'country': country,
                                'firstname': first,
                                'lastname': last,
                                'option': 'ignoreIfAlreadyExists'}
                           }]
                    }],
                1: [{'user': sso_username,
                     'domain': domain,
                     'requestID': str(uuid.uuid1()),
                     'do': [{'createFederatedID': {
                                'email': email,
                                'country': country,
                                'firstname': first,
                                'lastname': last,
                                'option': 'ignoreIfAlreadyExists'}
                           }]
                    }]
               }
    if '@' in sso_username:
        selection = j_format.get(0)
    else:
        selection = j_format.get(1)
    return selection

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
        
if __name__ == '__main__':
    rez = add_federated_id(UPN,EMAIL,FIRST,LAST,COUNTRY)
    print(rez)

