#!/usr/bin/python3

"""
   Send request to get todo list of employee
   Arguments: employee ID
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import json
    import sys

    id = sys.argv[1]
    name = ""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            html = html.decode('utf-8')
            html = json.loads(html)
            name = html.get('name')
            print(name)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

# Get tasks of the given user
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    req = urllib.request.Request(url)
    counter = 0  # Tasks counter
    tasks = []
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            html = json.loads(html.decode('utf-8'))
            for i in range(len(html)):
                if html[i].get('completed') is True:
                    counter = counter + 1
                    tasks.append(html[i].get('title'))
            print("Employee {} is done with tasks({}/{})".format(name,
                                                                 counter
                                                                 len(html)))

            # Print tasks
            for i in range(len(tasks)):
                print("\t {}".format(tasks[i]))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
# End of get tasks
