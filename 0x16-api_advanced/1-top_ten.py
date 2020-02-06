#!/usr/bin/python3

import requests


def top_ten(subreddit):
    headers = {'User-agent': ' JetBrains_official'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    req = requests.get(url, headers=headers, params=params)
    if req.status_code != 200:
        return 0
    req = req.json()
    hots = req['data']['children']
    for i in hots:
        print(i['data']['title'])
