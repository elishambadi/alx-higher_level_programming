#!/usr/bin/python3

"""
   Send request using requests package, extract a header value
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers['X-Request-Id'])
