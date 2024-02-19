#!/usr/bin/python3
"""Retrieve and display TODO list progress for a given employee ID."""

import requests as r
import sys

def get_todo_list(user_id):
    """Retrieve TODO list for the given user ID."""
    url = 'https://jsonplaceholder.typicode.com/'
    
    # Fetch user data
    user_data = r.get(url + 'users/{}'.format(user_id)).json()
    
    # Fetch TODO list for the user
    todo_list = r.get(url + 'todos', params={'userId': user_id}).json()
    
    return user_data, todo_list

def print_todo_progress(user_data, todo_list):
    """Print TODO list progress for the given user."""
    employee_name = user_data.get("name")
    completed_tasks = [task for task in todo_list if task.get('completed')]
    total_tasks = len(todo_list)
    completed_count = len(completed_tasks)
    
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_count, total_tasks))
    
    # Print completed tasks
    for title in completed_tasks:
        print("\t{}".format(title.get("title")))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    
    user_id = sys.argv[1]
    user_data, todo_list = get_todo_list(user_id)
    print_todo_progress(user_data, todo_list)
