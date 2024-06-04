#!/usr/bin/python3
"""
    write a script that returns information
    about his/her TODO list for a given
    employee ID
"""
# from urllib import request
import requests
from sys import argv

emp_id = argv[1]
base_url = 'https://jsonplaceholder.typicode.com/'
url_todo = f'{base_url}todos/?userId={emp_id}'
url_name = f'{base_url}/users/?id={emp_id}'

# Get employee name
emp_name = requests.get(url_name).json()
for attr in emp_name:
    name = attr['name']

# Get todo list
emp_todo = requests.get(url_todo).json()

all_tasks = len(emp_todo)
tasks = []
for i in emp_todo:
    if i['completed'] is True:
        tasks.append(i['title'])
 
done_task = len(tasks)
print(f'Employee {name} is done with tasks({done_task}/{all_tasks}): ')
for i in tasks:
    print(f'\t {i}')