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
import csv
import requests
from sys import argv


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
    output = {}
    for detail in details:
        status = detail.get('completed')
        title = detail.get('title')
        output.append([employee_id, USERNAME, status, title])
    return output


if __name__ == "__main__":
    output = get_data(argv[1])
    file = f'{argv[1]}.csv'

    try:
        with open(file, 'w') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for _ in output:
                writer.writerow(_)
    except NameError:
        print('File is not present')
