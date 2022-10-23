#!/usr/bin/python3

"""
   Send post request with email
   Arguments:
      1st: url to post to
      2nd: email to post to the url
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    email = sys.argv[2]
    url = sys.argv[1]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        html = response.read()
        html = html.decode("utf-8")
        print(html)
