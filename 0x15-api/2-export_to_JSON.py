#!/usr/bin/python3
"""
Python script that, using a given REST API.
"""

import json
import requests
from sys import argv

def export_to_json(employee_id, todos):
    filename = "{}.json".format(employee_id)
    with open(filename, 'w') as jsonfile:
        json.dump({employee_id: todos}, jsonfile)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    response_todos = requests.get(url_todos)

    if response_todos.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        exit(1)

    todos_data = response_todos.json()

    export_to_json(employee_id, todos_data)
    print("Data exported to {}.json".format(employee_id))
