#!/usr/bin/python3
"""
Python script that, using a given REST API.
"""

import csv
import requests
from sys import argv

def export_to_csv(employee_id, username, todos):
    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({'USER_ID': employee_id,
                             'USERNAME': username,
                             'TASK_COMPLETED_STATUS': str(todo['completed']),
                             'TASK_TITLE': todo['title']})

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

    export_to_csv(employee_id, user_data['username'], todos_data)
    print("Data exported to {}.csv".format(employee_id))
