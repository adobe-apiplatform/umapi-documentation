""" This script shows how to update an existing Adobe Admin Console account

License: MIT License

    Copyright (c) 2023 Adobe Inc.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

Documentation
    https://adobe-apiplatform.github.io/umapi-documentation/en/api/ActionsCmds.html
    POST /v2/usermanagement/action/{orgId}
"""

import uuid

import json
import requests

# access token obtained via OAuth S2S workflow
ACCESS_TOKEN = ''
CLIENT_ID = ''
ORG_ID = ''
# insert sample user data
CURRENT_EMAIL = 'current_email@claimed-domain.com'
NEW_EMAIL = 'new_email@claimed-domain.com'
NEW_USERNAME = 'new_username@dclaimed-domain.com'
# simulate call or make changes in Admin Console:
IS_TEST = 'true'
# default call management settings
UMAPI_URL = 'https://usermanagement.adobe.io/v2/usermanagement/action/'
MAX_RETRIES = 4
TIMEOUT = 120.0
RANDOM_MAX = 5
FIRST_DELAY = 3


def update_account(current_email, **kwargs):
    """ 
    First argument is always the current email of an existing account, followed
    by at least one of these keyword arguments: email, username, firstname, lastname
    for which the update is necessary
    """
    url = UMAPI_URL + ORG_ID + '?testOnly=' + IS_TEST
    method = 'POST'
    body = format_select(current_email, kwargs)
    print(f'{body}')
    if body == {}:
        print("No update requested")
    else:
        r = make_call(method, url, body)
        return r

def format_select(current_email, kwargs_dict):
    """ 
    helper function to build the body of the update POST call. Only this
    metadata can be updated: email, username, firstname, lastname
    """
    can_update = {'email': '',
                  'username': '',
                  'firstname': '',
                  'lastname': ''}
    # making sure just supported metadata gets used
    will_update = {k:v for k,v in kwargs_dict.items() if k in can_update.keys()}
    j_format = [{'user': current_email,
                 'requestID': str(uuid.uuid1()),
                 'do': [{'update': will_update }] }]
    return j_format

def make_call(method, url, body={}):
    """
    call manager function with retry mechanism which returns
    the API response as a dict
    """
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
    # current email as first argument followed by
    # any mix of username, email, firstname, lastname arguments
    # that require an update
    rez = update_account(CURRENT_EMAIL, 
                         username=NEW_USERNAME, 
                         email=NEW_EMAIL)
    print(rez)

