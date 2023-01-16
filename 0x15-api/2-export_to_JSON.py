#!/usr/bin/python3
"""
This file makes a request to a url
"""


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    import requests
    from sys import argv
    import json

    if len(argv) > 1:
        uid = argv[1]
        r = requests.get('{}/{}/{}'.format(base_url, 'users', uid))

        user = r.json()
        r = requests.get('{}/{}?userId={}'.format(
            base_url, 'todos', uid))
        todos = r.json()
        header_format = 'Employee {} is done with task({}/{}):'
        c_todos = sum(todo['completed'] for todo in todos)
        result = {'{}'.format(uid): []}
        for todo in todos:
            data = {'task': todo['title'],
                    'completed': todo['completed'],
                    'username': user['username']}
            result[uid].append(data)
        with open('{}.json'.format(uid), 'w') as file:
            json.dump(result, file)
