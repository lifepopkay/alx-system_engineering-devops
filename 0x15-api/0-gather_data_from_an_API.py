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
base_url = 'https://jsonplaceholder.typicode.com/todos'
url_todo = f'{base_url}/?userId={emp_id}'
url_name = f'{base_url}/users/{emp_id}'

# Get employee name
emp_name = requests.get(url_name).json()
print(emp_name)

# Get todo list
emp_todo = requests.get(url_todo).json()
print(emp_todo)
