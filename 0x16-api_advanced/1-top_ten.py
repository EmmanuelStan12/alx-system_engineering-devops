#!/usr/bin/python3
"""
Prints the top ten hottest posts
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 given subreddits
    """
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {
            "User-Agent": "0x16-api_advanced"
    }
    params = {
            "limit": 10
    }
    result = requests.get(url, headers=headers, params=params,
                          allow_redirects=False)
    if result.status_code == 404:
        print("None")
        return
    data = result.json().get("data")
    if data is not None:
        for post in data.get('children'):
            print(post.get('data').get('title'))
