
#!/usr/bin/python3
"""Fetches the titles of the 10 hottest posts from a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts[:10]:
            print(post.get('data', {}).get('title'))
    else:
        print("OK")
