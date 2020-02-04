#!/usr/bin/python3
"""  Python script to export data in the CSV format """

import csv
import json
import requests
import sys


if __name__ == "__main__":
    r0 = requests.get('https://jsonplaceholder.typicode.com/todos',
                      params={'userId': sys.argv[1]})
    r1 = requests.get('https://jsonplaceholder.typicode.com/users',
                      params={'id': sys.argv[1]})

    t = r0.json()
    u = r1.json()

    l = []
    dic = {}
    for i in t:
        dic["task"] = i['title']
        dic["completed"] = i['completed']
        dic["username"] = u[0]['username']
        l.append(dic)
    j = {}
    j[sys.argv[1]] = l
    with open("{}.json".format(sys.argv[1]), 'w') as jf:
        json.dump(j, jf)
