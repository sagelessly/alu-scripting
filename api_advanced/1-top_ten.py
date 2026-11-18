#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a given subreddit.

    Print None if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-scripting/0.0.1 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        children = response.json().get("data", {}).get("children", [])
        if not children:
            print(None)
            return
        for child in children[:10]:
            print(child.get("data", {}).get("title"))
    except Exception:
        print(None)
