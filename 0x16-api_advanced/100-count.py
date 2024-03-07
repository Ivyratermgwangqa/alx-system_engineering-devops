#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """Prints a sorted count of given keywords in hot articles of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/1.0"}  # Set a custom User-Agent to avoid Too Many Requests error
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        for post in children:
            title = post["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title:
                    if word.lower() in word_count:
                        word_count[word.lower()] += 1
                    else:
                        word_count[word.lower()] = 1
        after = data["data"]["after"]
        if after is not None:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print(f"{word}: {count}")
    else:
        print(None)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())
