#!/usr/bin/python3
"""
This recursively checks for subreddit
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """
    This returns a list of subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": '0x16-api_advanced'
    }
    params = {
            "after": after,
            "count": count,
            "limit": 100
    }
    result = requests.get(url, headers=headers, params=params,
                          allow_redirects=False)
    if result.status_code == 404:
        return None

    data = result.json().get('data')
    after = data.get('after')
    count = count + data.get('dist', 0)
    for post in data.get('children'):
        hot_list.append(post.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
