#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all articles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "MyBot/1.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        for post in children:
            hot_list.append(post["data"]["title"])
        after = data["data"]["after"]
        if after is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
