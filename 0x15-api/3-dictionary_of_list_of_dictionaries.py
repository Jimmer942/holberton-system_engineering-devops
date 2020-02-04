#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """

import json
import requests
import sys

if __name__ == "__main__":
    r0 = requests.get('https://jsonplaceholder.typicode.com/todos')
    r1 = requests.get('https://jsonplaceholder.typicode.com/users')

    t = r0.json()
    u = r1.json()

    dic_user = {}
    dic_info = {}
    info = []
    for i in u:
        uname = i['username']

        for j in t:
            if j['userId'] == i['id']:
                dic_info['username'] = uname
                dic_info['task'] = j['title']
                dic_info['completed'] = j['completed']
                info.append(dic_info)
        dic_user[i['id']] = info

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dic_user, f)
