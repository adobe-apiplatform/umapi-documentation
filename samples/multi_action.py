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
import csv
import math

import json
import requests

# obtained via JWT or OAuth S2S workflow
ACCESS_TOKEN = ''
CLIENT_ID = ''
ORG_ID = ''
# simulate call or make changes in Admin Console:
IS_TEST = 'true'
SOURCE_CSV = 'source.csv'
# control hard or soft delete (with or without loss of cloud assets)
PERMANENT_DELETE = False
# default call management settings
UMAPI_URL = 'https://usermanagement.adobe.io/v2/usermanagement/action/'
MAX_RETRIES = 4
TIMEOUT = 120.0
RANDOM_MAX = 5
FIRST_DELAY = 3

def multi_action(csv_file):
    url = UMAPI_URL + ORG_ID + '?testOnly=' + IS_TEST
    method = 'POST'
    actions = prepare_body(csv_file)
    if actions:
        batches = math.ceil(len(actions)/10)
        index = 0
        done = False
        # can't send more than 10 actions in an API call,
        # so splitting the task in bacthes of max 10 actions
        while not done:
            print(f'Sending batch {int(index/10) + 1}/{batches}')
            body = actions[index:index+10]
            print(make_call(method, url, body))
            index += 10
            if index/10 + 1 > batches:
                done = True
    print('All done')

def prepare_body(source_file):
    # helper function to prepare call's body and create a list of 
    # actions to proecess
    # for demo, choosing source.csv file as input
    actions = []
    with open(source_file) as csvfile:
        readout = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in readout:
            # column labels from csv file
            upn = row['upn']
            mail = row['mail']
            code = row['country_code']
            first = row['firstname']
            last = row['lastname']
            groups = row['groups']
            if groups:
                groups = groups.split(',')
            else:
                groups = []
            action = {'user': upn,
                      'requestID': str(uuid.uuid1()),
                      'do': [
                             {'createFederatedID': {
                                'email': mail,
                                'country': code,
                                'firstname': first,
                                'lastname': last,
                                'option': 'ignoreIfAlreadyExists'}
                             },
                             {'add': {'group': groups }},
                             {'removeFromOrg': {'deleteAccount': True}}
                            ]
                     }
            actions.append(action)
    return actions

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
    # use an existing account's email value from Admin Console
    multi_action(SOURCE_CSV)

