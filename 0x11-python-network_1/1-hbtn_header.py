#!/usr/bin/python3

"""
   Use urllib to send request
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        info = dict(response.info())
        print(info.get('X-Request-Id'))
