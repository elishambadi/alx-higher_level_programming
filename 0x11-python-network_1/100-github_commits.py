#!/usr/bin/python3

"""
   Send requests to Github API; returns 10 latest commits
   Arguments:
      r_name: Repository name
      o_name: Owner name
"""

if __name__ == "__main__":
    import requests
    import sys

    r_name = sys.argv[1]
    o_name = sys.argv[2]

    auth = "Bearer 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"
    headers = {'Accept': 'application/vnd.github+json', 'Authorization': auth}

    url = "https://api.github.com/repos/"+o_name+"/"+r_name+"/commits"

    res = requests.get(url, headers=headers)
    res = res.json()

    for i in range(10):
        print("{}: {}".format(res[i]["sha"], res[i]["commit"]["author"]["name"]))
