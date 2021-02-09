# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 08:34:15 2021

@author: Acer
"""

import urllib.parse
import requests

main_api="https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Loja"
key ="xxECUq7fIubJBImLAMjqZNp9qNzDnA0m"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
print("URL: " + (url))

json_data = requests.get (url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print ("API Status: " + str(json_status) + " = A successful route call.\n")