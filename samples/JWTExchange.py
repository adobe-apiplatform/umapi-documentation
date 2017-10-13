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
    from urllib import urlencode
if sys.version_info[0] >= 3:
    from configparser import RawConfigParser
    from urllib.parse import urlencode
import time
import jwt
import requests
import json

# read configuration file
config_file_name = "usermanagement.config"
config = RawConfigParser()
config.read(config_file_name)

# read server parameters
ims_host = config.get("server", "ims_host")
ims_endpoint_jwt = config.get("server", "ims_endpoint_jwt")

# read enterprise parameters
org_id = config.get("enterprise", "org_id")
tech_acct = config.get("enterprise", "tech_acct")
api_key = config.get("enterprise", "api_key")
client_id = api_key
client_secret = config.get("enterprise", "client_secret")
priv_key_filename = config.get("enterprise", "priv_key_filename")

# CREATE JSON WEB TOKEN
print("Generating JSON Web Token...")

# Set the expiration time for the JSON Web Token to one day from the current time. This is a typical and recommended validity period.
expiry_time = int(time.time()) + 60*60*24

# create payload
payload = {
    'exp' : expiry_time,
    'iss' : org_id,
    'sub' : tech_acct,
    'aud' : "https://" + ims_host + "/c/" + api_key
}

# define scopes
scopes = [ "ent_user_sdk" ]

# add scopes to the payload
for scope in scopes:
    payload["https://" + ims_host + "/s/" + scope] = True

# Read the private key we will use to sign the JWT.
priv_key_file = open(priv_key_filename)
priv_key = priv_key_file.read()
priv_key_file.close()

# create JSON Web Token, signing it with the private key.
jwt_token = jwt.encode(payload, priv_key, algorithm='RS256')

# decode bytes into string
jwt_token = jwt_token.decode("utf-8")

# write JSON Web Token to configuration file. For debugging purposes, we store the result. 
#In practice, you should never print or retain JWTs that you create.
config.set("enterprise", "jwt_token", jwt_token)
config_file = open(config_file_name, "w")
config.write(config_file)
config_file.close()

# CREATE JSON WEB TOKEN END


# REQUEST ACCESS TOKEN
print("Requesting access token...")

# method parameters. The credentials are placed in the body of the POST request. Notice that the "client_id" value is your API key.
url = "https://" + ims_host + ims_endpoint_jwt
headers = {
    "Content-Type" : "application/x-www-form-urlencoded",
    "Cache-Control" : "no-cache"
}
body_credentials = {
    "client_id" : client_id,
    "client_secret" : client_secret,
    "jwt_token" : jwt_token
}
body = urlencode(body_credentials)

# send http request
res = requests.post(url, headers=headers, data=body)

# evaluate response
if res.status_code == 200:
    # extract token
    access_token = json.loads(res.text)['access_token']

    # write access token to configuration file
    config.set("enterprise", "access_token", access_token)
    config_file = open(config_file_name, "w")
    config.write(config_file)
    config_file.close()

    # print access token
    print("Your access token is:")
    print(access_token)
    exit(res.status_code);
else:
    # print response
    print(res.status_code)
    print(res.headers)
    print(res.text)
    exit(res.status_code);
