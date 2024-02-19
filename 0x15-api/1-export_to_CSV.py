#!/usr/bin/python3
"""
Export data in the CSV format
"""

import csv
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

    with open('{}.csv'.format(user_id), mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for task in todo_data:
            writer.writerow([user_id, employee_name, task.get('completed'), task.get('title')])
