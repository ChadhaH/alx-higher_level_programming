#!/usr/bin/python3
"""
    a Python script that takes in a letter
    and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import sys
    import requests

    leter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": leter}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
