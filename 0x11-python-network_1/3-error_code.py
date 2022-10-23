#!/usr/bin/python3

"""
   Send request and handle HTTPError error
   Arguments: URL only
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            html = html.decode("utf-8")
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
