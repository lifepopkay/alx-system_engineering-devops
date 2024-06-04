#!/usr/bin/python3
"""
    write a script that returns information
    about his/her TODO list for a given
    employee ID
"""
import requests
from sys import argv


def get_data(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    url_todo = f'{base_url}todos/?userId={employee_id}'
    url_name = f'{base_url}/users/?id={employee_id}'

    # Get employee name
    emp_name = requests.get(url_name).json()[0]['name']

    # Get todo list
    emp_todo = requests.get(url_todo).json()

    all_tasks = len(emp_todo)
    tasks = []
    for i in emp_todo:
        if i['completed'] is True:
            tasks.append(i['title'])

    done_task = len(tasks)
    print(f'Employee {emp_name} is done with tasks({done_task}/{all_tasks}):')
    for i in tasks:
        print(f' \t{i}')


if __name__ == "__main__":
    get_data(argv[1])
