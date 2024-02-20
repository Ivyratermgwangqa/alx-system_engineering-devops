#!/usr/bin/python3
"""
Export data to CSV format.
"""
import csv
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

    employee_name = user_data.get('name')
    if not employee_name:
        print("Employee name not found for ID: {}".format(employee_id))
        sys.exit(1)

    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([employee_id, employee_name, todo.get('completed'), todo.get('title')])

    print("Tasks exported to", filename)
