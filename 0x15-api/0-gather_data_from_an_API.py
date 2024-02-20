#!/usr/bin/python3
"""
Python script that, using a given REST API.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    response_user = requests.get(url_user)
    response_todos = requests.get(url_todos)

    if response_user.status_code != 200:
        print("Error: Unable to fetch user data")
        exit(1)

    if response_todos.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        exit(1)

    user_data = response_user.json()
    todos_data = response_todos.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]

    print("Employee {} is done with tasks({}/{}):".format(user_data['name'], len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task['title']))
