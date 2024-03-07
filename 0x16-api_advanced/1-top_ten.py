#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/1.0"}  # Set a custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"][:10]:
            print(post["data"]["title"])
    else:
        print(None)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
