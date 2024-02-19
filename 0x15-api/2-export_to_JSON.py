#!/usr/bin/python3
"""
Export data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get('name')

    json_data = {user_id: []}
    for task in todo_data:
        json_data[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    with open('{}.json'.format(user_id), mode='w') as file:
        json.dump(json_data, file)
