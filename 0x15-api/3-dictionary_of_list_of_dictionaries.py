#!/usr/bin/python3
"""
This file makes a request to a url
"""


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    import requests
    import json

    r = requests.get('{}/{}'.format(base_url, 'users'))
    users = r.json()
    result = {}
    for user in users:
        uid = '{}'.format(user['id'])
        result[uid] = []
        r = requests.get('{}/{}?userId={}'
                         .format(base_url, 'todos', uid))
        todos = r.json()
        for todo in todos:
            data = {'username': user['username'],
                    'task': todo['title'],
                    'completed': todo['completed']}
            result[uid].append(data)
    with open('todo_all_employees.json', 'w') as file:
        json.dump(result, file)
