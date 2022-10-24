#!/usr/bin/python3

"""
   Send requests to API, handle KeyError
   Arguments:
      Student ID
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        user = ""
        print("No result")
        exit(0)
    else:
        user = sys.argv[1]
        payload = {'q': user}

    r = requests.post(url, data=payload)
    res = r.json()
    try:
        if len(res) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res["id"], res["name"]))
    except KeyError:
        print("Not a valid JSON")
