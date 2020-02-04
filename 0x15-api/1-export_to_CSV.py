#!/usr/bin/python3
"""  Python script to export data in the CSV format """

import requests
import sys
import csv

if __name__ == "__main__":
    r0 = requests.get('https://jsonplaceholder.typicode.com/todos',
                      params={'userId': sys.argv[1]})
    r1 = requests.get('https://jsonplaceholder.typicode.com/users',
                      params={'id': sys.argv[1]})

    t = r0.json()
    u = r1.json()

    with open("{}.csv".format(sys.argv[1]), 'w', newline='') as csvfile:
        cvs_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in t:
            cvs_writer.writerow([int(sys.argv[1]), u[0]['username'],
                                 i['completed'], i['title']])
