""" This script shows how to obtain an access token using the OAuth Server-to-Server workflow

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

Documentation:
    https://developer.adobe.com/developer-console/docs/guides/authentication
"""

import json

import requests

CLIENT_ID = ''
CLIENT_SECRET = ''
URL = 'https://ims-na1.adobelogin.com/ims/token/v2'
def get_authorization():
    b = ('grant_type=client_credentials&'
         'client_id=' + CLIENT_ID + '&'
         'client_secret=' + CLIENT_SECRET + '&'
         'scope=openid,AdobeID,user_management_sdk')
    h = {'Accept': 'application/json',
         'Content-Type': 'application/x-www-form-urlencoded'}
    
    r = requests.request('POST', URL, headers=h, data=b)
    return json.loads(r.text)

if __name__ == '__main__':
   req = get_authorization()
   print(req)
