#!/usr/bin/python3
"""
    convert response into CSV
    Format:
          "USER_ID",\
          "USERNAME",\
          "TASK_COMPLETED_STATUS",\
          "TASK_TITLE"
    Filename:
            USER_ID.csv
"""
import json
import requests


def to_dict(data):
    new_list = {}
    for item in data:
        for key, val in item.items():
            new_list[key] = val
        return new_list


def get_data(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    url_todo = f'{base_url}todos/?userId={employee_id}'
    url_name = f'{base_url}/users/?id={employee_id}'

    # Get employee name
    response = requests.get(url_name).json()
    USERNAME = to_dict(response).get('username')

    # Get task details
    response = requests.get(url_todo).json()
    details = response
    output = []
    for detail in details:
        status = detail.get('completed')
        title = detail.get('title')
        dict_task = {'username': USERNAME, 'task': title, 'completed': status}
        output.append(dict_task)
    return output


if __name__ == "__main__":
    all_employees = {}
    for i in range(1, 11):
        employee = {str(i): get_data(i)}
        all_employees.update(employee)
    file = 'todo_all_employees.json'

    with open(file, 'w') as jsonfile:
        json.dump(all_employees, jsonfile, indent=4)
