#!/usr/bin/python3

"""
   Send request using requests package, handling errors
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv == 0):
        user = ""
    else
        user = sys.argv[1]
    payload = {'q':user}

    r = requests.post(url, data=payload)
    print(r.text)
