#!/usr/bin/python3

"""
   Send requests to Github API; returns ID
   Arguments:
      uname: Username
      pass_:  Password
"""

if __name__ == "__main__":
    import requests
    import sys

    uname = sys.argv[1]
    pass_ = sys.argv[2]

    auth = "Bearer "+pass_
    payload = {'username': uname}
    headers = {'Accept': 'application/vnd.github+json', 'Authorization': auth}

    url = "https://api.github.com/users/"+uname

    res = requests.get(url, params=payload, headers=headers)
    if res.status_code == 200:
        print(res.json()["id"])
    else:
        print("None")
