#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    # Get todos data
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos_response.json()

    # Get users data
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users_response.json()

    # Create a dictionary to store tasks for each user
    todo_dict = {}
    for user in users:
        user_id = user.get('id')
        todo_dict[user_id] = []

    # Assign tasks to the corresponding user ID
    for todo in todos:
        user_id = todo.get('userId')
        todo_dict[user_id].append({
            "username": next((user.get('username') for user in users if user.get('id') == user_id), None),
            "task": todo.get('title'),
            "completed": todo.get('completed')
        })

    # Write the data to a JSON file
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(todo_dict, json_file, indent=4)
