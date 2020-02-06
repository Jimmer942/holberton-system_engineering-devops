#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after=""):
    headers = {'User-agent': ' JetBrains_official'}
    params = {'after': after}
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    req = requests.get(url, headers=headers, params=params)
    if req.status_code != 200:
        return None
    req = req.json()
    hots = req['data']['children']
    for i in hots:
        hot_list.append(i['data']['title'])
    page = req['data']['after']
    if page is not None:
        recurse(subreddit, hot_list, page)
    return hot_list
