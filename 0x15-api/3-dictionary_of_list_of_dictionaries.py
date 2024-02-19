#!/usr/bin/python3
"""A Script that, uses a REST API, for all employee IDs, returns
information about their TODO list progress and exports data
in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    session_request = requests.Session()

    users_response = session_request.get(url)
    users_data = users_response.json()

    all_employee_data = {}

    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')

        todo_url = (
            'https://jsonplaceholder.typicode.com/users/{}/todos'
            .format(user_id)
        )
        todo_response = session_request.get(todo_url)
        todo_data = todo_response.json()

        user_tasks = []

        for task in todo_data:
            user_tasks.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

        all_employee_data[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employee_data, jsonfile, indent=4)
