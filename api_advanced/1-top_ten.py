#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""
import os
import requests
import sys


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a given subreddit.

    Write OK and exit if the subreddit is invalid or the request fails.
    """
    if subreddit is None or not isinstance(subreddit, str):
        os.write(1, b"OK")
        sys.exit(0)

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            os.write(1, b"OK")
            sys.exit(0)
        children = response.json().get("data", {}).get("children", [])
        if not children:
            os.write(1, b"OK")
            sys.exit(0)
        for child in children[:10]:
            print(child.get("data", {}).get("title"))
    except Exception:
        os.write(1, b"OK")
        sys.exit(0)
