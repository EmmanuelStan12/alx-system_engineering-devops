#!/usr/bin/python3
"""
This shows how many subscribers are on Reddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a subreddit
    """
    url = 'http://www.reddit.com/r/{}/about.json'
    result = requests.get(url.format(subreddit),
                          headers={'User-Agent': '0x16-api_advanced'}).json()
    data = result.get('data', None)
    if not data:
        return 0
    num = data.get('subscribers', 0)
    return num
