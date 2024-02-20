#!/usr/bin/python3
"""
Export data to JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    user_info = {
        str(employee_id): [
            {
                'task': todo.get('title'),
                'completed': todo.get('completed'),
                'username': user_data.get('username')
            }
            for todo in todos_data
        ]
    }

    filename = '{}.json'.format(employee_id)
    with open(filename, 'w') as file:
        json.dump(user_info, file)

    print("Tasks exported to", filename)
