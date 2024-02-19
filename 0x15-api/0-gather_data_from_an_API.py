#!/usr/bin/python3
"""
A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    session_request = requests.Session()

    employee_id = argv[1]
    todo_url = ('https://jsonplaceholder.typicode.com/users/{}/'
                'todos').format(employee_id)
    name_url = ('https://jsonplaceholder.typicode.com/users/{}'
                .format(employee_id))

    todo_response = session_request.get(todo_url)
    name_response = session_request.get(name_url)

    todo_data = todo_response.json()
    employee_name = name_response.json()['name']

    total_tasks_completed = 0

    for task in todo_data:
        if task['completed']:
            total_tasks_completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total_tasks_completed, len(todo_data)))

    for task in todo_data:
        if task['completed']:
            print("\t " + task.get('title'))
