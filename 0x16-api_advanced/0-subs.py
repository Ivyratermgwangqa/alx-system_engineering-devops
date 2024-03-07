#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    headers = {'User-agent': ' JetBrains_official'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url, headers=headers)
    if req.status_code != 200:
        return 0
    req = req.json()
    return req['data']['subscribers']
