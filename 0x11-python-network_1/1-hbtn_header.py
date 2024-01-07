#!/usr/bin/python3
"""
     a Python script that takes in a URL
     sends a request to the URL and displays the value of
     the X-Request-Id variable found in the header of the response.
"""
import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    html_request = request.Request(url)
    with request.urlopen(html_request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
