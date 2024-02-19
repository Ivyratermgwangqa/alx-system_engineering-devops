#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url, params={'userId': user_id})

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get('username')  # Use 'username' instead of 'name'
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t{}".format(task.get('title')))  # Adjust formatting for task titles
