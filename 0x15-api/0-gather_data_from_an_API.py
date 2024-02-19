#!/usr/bin/python3
"""Retrieve and display TODO list progress for a given employee ID."""
import requests as req
import sys

if __name__ == '__main__':
    # Retrieve user information
    user_id = sys.argv[1]
    user_response = req.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Retrieve user's TODO list
    todo_response = req.get('https://jsonplaceholder.typicode.com/todos',
                            params={'userId': user_id})
    todo_data = todo_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todo_data if task.get('completed')]

    # Print employee progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todo_data)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
