#!/usr/bin/python3
"""
A Script that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
exporting data in the CSV format.
"""

import csv
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

    total_tasks_completed = 0

    for task in todo_data:
        if task['completed']:
            total_tasks_completed += 1

    file_csv = '{}.csv'.format(employee_id)

    with open(file_csv, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo_data:
            writer.writerow([employee_id, employee_username,
                             task.get('completed'), task.get('title')])
