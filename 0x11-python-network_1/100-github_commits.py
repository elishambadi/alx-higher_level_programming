#!/usr/bin/python3

"""
   Send requests to Github API; returns last 10 commits
   Arguments:
      r_name: Repository Name
      o_name: Owner Name
"""

if __name__ == "__main__":
    import requests
    import sys

    r_name = sys.argv[1]
    o_name = sys.argv[2]

    # Auth section
    token = "Bearer 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"
    headers = {'Accept': 'application/vnd.github+json', 'Authorization': token}

    url = "https://api.github.com/repos/"+o_name+"/"+r_name+"/commits"
    params = {'per_page': 10}

    res = requests.get(url, params=params, headers=headers)
    json = res.json()

    for i in range(10):
        print("{}: {}".format(json[i]["sha"],
                              json[i]["commit"]["author"]["name"]))
