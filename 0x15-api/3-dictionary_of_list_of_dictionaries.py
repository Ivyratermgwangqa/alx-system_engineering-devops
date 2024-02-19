#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()

    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = users_response.json()

    todo_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        todo_dict[user_id] = []
        for todo in todos:
            if todo.get('userId') == user_id:
                todo_dict[user_id].append({
                    "username": username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                })

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(todo_dict, json_file, indent=4)
