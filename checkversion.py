#!/usr/bin/env python

from __future__ import print_function

import requests

print(requests.__version__)

response = requests.get("http://google.com")

print(response.status_code)
print(response.text)