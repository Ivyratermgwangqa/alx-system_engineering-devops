#!/usr/bin/python3

import requests as r


def top_ten(subreddit):
    """
    Print top 10 posts from the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) "
                      "Gecko/20100101 Firefox/73.0"
    }
    params = {"limit": 10}
    response = r.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for top in results.get("children"):
        print(top.get("data").get("title"))


if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    top_ten(subreddit_name)
