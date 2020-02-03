#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """

import requests
import sys

if __name__ == "__main__":
    r0 = requests.get('https://jsonplaceholder.typicode.com/todos',
                      params={'userId': sys.argv[1]})
    r1 = requests.get('https://jsonplaceholder.typicode.com/users',
                      params={'id': sys.argv[1]})

    t = r0.json()
    u = r1.json()

    f = []
    for i in t:
        if i['completed'] is True:
            f.append(i)

    print("Employee {} is done with tasks({}/{})".
          format(u[0]['name'], len(f), len(t)))
    if len(f) > 0:
        for i in f:
            print("\t {}".format(i['title']))
