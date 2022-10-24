#!/usr/bin/python3

"""
   Send request using requests package, with email
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    r = requests.post(url, json=payload)
    print(r.text)
