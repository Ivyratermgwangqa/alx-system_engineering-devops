#!/usr/bin/python3
"""
100-count
"""
import operator
import requests


def count_w(word, title):
    words = title.split()
    count = 0
    for w in words:
        if w.upper() == word.upper():
            count += 1
    return count


def count_words(subreddit, word_list, nexT="", count={}):
    if len(count) == 0:
        n = [0] * len(word_list)
        count = dict(zip(word_list, n))

    headers = {'User-agent': 'Alb4tr02'}
    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json" + nexT
    req = requests.get(url, headers=headers)
    req1 = requests.get("https://www.reddit.com/r/" +
                        subreddit, headers=headers)

    if req1.status_code != 200:
        return

    json_data = req.json()
    if 'error' in json_data:
        return

    for post in json_data['data']['children']:
        title = post['data']['title']
        for word in word_list:
            count[word] += count_w(word, title)

    if json_data['data']['after'] is not None:
        return count_words(subreddit, word_list, "?after=" + json_data['data']['after'], count)
    else:
        aux = sorted(count.items(), key=operator.itemgetter(0), reverse=False)
        aux1 = {}
        flag = True
        lk = []
        lv = []
        for element in aux:
            lk.append(element[0])
            lv.append(element[1])
        aux1 = dict(zip(lk, lv))
        aux = sorted(aux1.items(), key=operator.itemgetter(1), reverse=True)
        for element in aux:
            if element[1] != 0:
                print("{}: {}".format(element[0], element[1]))
                flag = False
        if flag:
            print("")
