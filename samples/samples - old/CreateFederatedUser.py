#!/usr/bin/python

#*************************************************************************
#
# ADOBE CONFIDENTIAL
# ___________________
#
#  Copyright 2017 Adobe Systems Incorporated
#  All Rights Reserved.
#
# NOTICE:  Adobe permits you to use, modify, and distribute this file in 
# accordance with the terms of the Adobe license agreement accompanying it.
# If you have received this file from a source other than Adobe, then your
# use, modification, or distribution of it requires the prior written
# permission of Adobe.
#**************************************************************************

import sys
if sys.version_info[0] == 2:
    from ConfigParser import RawConfigParser
if sys.version_info[0] >= 3:
    from configparser import RawConfigParser
import json
import requests
import random
import string

# read configuration file
config_file_name = "usermanagement.config"
config = RawConfigParser()
config.read(config_file_name)

# server parameters
host = config.get("server", "host")
endpoint = config.get("server", "endpoint")

# enterprise parameters
domain = config.get("enterprise", "fed_domain")
org_id = config.get("enterprise", "org_id")
api_key = config.get("enterprise", "api_key")
access_token = config.get("enterprise", "access_token")

# method parameters
url = "https://" + host + endpoint + "/action/" + org_id
headers = {
    "Content-type" : "application/json",
    "Accept" : "application/json",
    "x-api-key" : api_key,
    "Authorization" : "Bearer " + access_token
    }

user_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
json_data = \
[
  {
    "user" : user_string,
    "domain" : domain,
    "do" : [
      {
        "createFederatedID" : {
          "email" : user_string + "@" + domain,
          "country" : "US",
          "firstname" : "John",
          "lastname" : "Doe"
        }
      }
    ]
  }
]

# prepare body
body = json.dumps(json_data)
print("Sending following request body to User Management Action API: " + body)

# send http request
res = requests.post(url, headers=headers, data=body)

# print response
print(res.status_code)
print(res.headers)
print(res.text)

# parse response body
if res.status_code == 200:
  res_json_data = json.loads(res.text)
  result = res_json_data["result"]
  if result == "success":
    print("Success");

exit(res.status_code)