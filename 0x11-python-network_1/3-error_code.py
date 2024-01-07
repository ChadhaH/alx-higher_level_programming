#!/usr/bin/python3
"""
    a Python script that takes in a URL
    sends a request to the URL
    and displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import sys
    from urllib import request
    from urllib import error

    url = sys.argv[1]
    html_request = request.Request(url)
    try:
        with request.urlopen(html_request) as resp:
            print(resp.read().decode("ascii"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
