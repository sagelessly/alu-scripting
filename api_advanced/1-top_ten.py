#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a given subreddit.

    Print nothing if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return
        children = response.json().get("data", {}).get("children", [])
        for child in children[:10]:
            print(child.get("data", {}).get("title"))
    except Exception:
        return
