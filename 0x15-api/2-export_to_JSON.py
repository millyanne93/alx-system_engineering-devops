#!/usr/bin/python3
"""
A Script that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
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
    employee_username = name_response.json()['username']

    tasks = []

    for task in todo_data:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_username
        })

    user_data = {
        employee_id: tasks
    }

    file_json = '{}.json'.format(employee_id)

    with open(file_json, "w") as jsonfile:
        json.dump(user_data, jsonfile, indent=4)
