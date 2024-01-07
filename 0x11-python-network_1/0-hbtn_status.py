#!/usr/bin/python3
"""
    a Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    from urllib import request
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as resp:
        html_content = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(html_content)))
        print("\t- content: {}".format(html_content))
        print("\t- utf8 content: {}".format(html_content.decode('utf-8')))
