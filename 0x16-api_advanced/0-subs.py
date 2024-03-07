#!/usr/bin/python3

"""
This module retrieves the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) \
        Gecko/20100101 Firefox/73.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(f"Number of subscribers in r/{subreddit}: "
              f"{number_of_subscribers(subreddit)}")
