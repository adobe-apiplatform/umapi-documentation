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


import json
from time import time

import jwt
import requests

CLIENT_ID = ''
CLIENT_SECRET = ''
TECH_ACCT_ID = ''
ORG_ID = ''
# use absolute path, or leave as is if the file is in same folder
PRIV_KEY_PATH = 'private.key'
URL = 'https://ims-na1.adobelogin.com/ims/exchange/jwt'

def get_authorization():
    # set 1 hour expiration time for the JWT
    exp_time = int(time()) + 60 * 60
    payload = {'exp' : exp_time,
               'iss' : ORG_ID,
               'sub' : TECH_ACCT_ID,
               'aud' : 'https://ims-na1.adobelogin.com/c/' + CLIENT_ID}
    payload['https://ims-na1.adobelogin.com/s/ent_user_sdk'] = True
    with open(PRIV_KEY_PATH) as f:
            priv_key = f.read()
    # issue local JWT
    jwt_token = jwt.encode(payload, priv_key, algorithm='RS256')
    # exchange for an access_token
    h = {'Accept': 'application/json',
         'Content-Type': 'application/x-www-form-urlencoded'}
    b = ('client_id=' + CLIENT_ID + '&'
         'client_secret=' + CLIENT_SECRET + '&'
         'jwt_token=' + jwt_token)
    r = requests.request('POST', URL, headers=h, data=b)
    return json.loads(r.text)

if __name__ == '__main__':
   req = get_authorization()
   print(req)
