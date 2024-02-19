#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    # Base URL for API requests
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Retrieve user's TODO list
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Filter completed tasks
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]

    # Print user progress
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    
    # Print completed tasks
    for task in completed_tasks:
        print("\t", task)
