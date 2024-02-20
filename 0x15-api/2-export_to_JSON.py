#!/usr/bin/python3
"""
Export data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    # Check if user ID is provided as a command-line argument
    if len(argv) != 2:
        print("Usage: {} <user_id>".format(argv[0]))
        exit(1)

    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Failed to fetch user data")
        exit(1)
    user_data = user_response.json()

    # Fetch todo data for the user
    todo_response = requests.get(todo_url, params={'userId': user_id})
    if todo_response.status_code != 200:
        print("Error: Failed to fetch TODO data")
        exit(1)
    todo_data = todo_response.json()

    # Extract employee name
    employee_name = user_data.get('name')

    # Prepare JSON data
    json_data = {
        "user_id": user_id,
        "tasks": []
    }
    for task in todo_data:
        json_data["tasks"].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    # Write JSON data to a file
    output_file = '{}.json'.format(user_id)
    with open(output_file, mode='w') as file:
        json.dump(json_data, file, indent=4)

    print("Data exported to", output_file)
