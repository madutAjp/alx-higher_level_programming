#!/usr/bin/python3
#a python script that fetches

import urllib.request
req = urllib.request.Request(https://alx-intranet.hbtn.io/status)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
