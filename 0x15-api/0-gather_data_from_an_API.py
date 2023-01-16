#!/usr/bin/python3
"""
This file makes a request to a url
"""


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) > 1:
        user_id = argv[1]
        r = requests.get('{}/{}/{}'.format(base_url, 'users', user_id))

        user_data = r.json()
        r = requests.get('{}/{}?userId={}'.format(base_url, 'todos', user_id))
        todos = r.json()
        header_format = 'Employee {} is done with tasks({}/{}):'
        c_todos = sum(todo['completed'] for todo in todos)
        print(header_format.format(user_data['name'], c_todos, len(todos)))
        for todo in todos:
            if todo['completed']:
                print('\t {}'.format(todo['title']))
