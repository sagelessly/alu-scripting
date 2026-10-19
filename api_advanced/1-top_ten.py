#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the tiles of the first 10 hot posts for a subreddit."""

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)

    response = requests.get(
        subreddit_url,
        headers=headers,
        allow-redirects=False
    )

    if response.status_code == 200:
        json_data = response.json()

        posts = json_data.get('data', {}.get('children', [])
                              
        for post in posts [:10]:
            print( post.get('data', {}).get('title'))
            )
    else:
        return
