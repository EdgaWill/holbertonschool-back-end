#!/usr/bin/python3
''' Export to JSON '''

import json
import requests
from sys import argv


def get_api():
    ''' Gather data from an API '''
    url = 'https://jsonplaceholder.typicode.com/'
    uid = argv[1]

    # get a specific user from users in jsonplaceholder
    usr = requests.get(url + 'users/{}'.format(uid)).json()
    # make a query string to get tasks based on user id
    man = requests.get(url + 'todos', params={'userId': uid}).json()

    with open('{}.json'.format(uid), 'w') as file:
        obj = {uid: []}
        for employee in man:
            tmp_obj = {
                    'task': employee.get('title'),
                    'completed': employee.get('completed'),
                    'username': usr.get('username')
                    }
            obj[uid].append(tmp_obj)
        # serialize an onject into a JSON stream
        json.dump(obj, file)


if __name__ == '__main__':
    get_api()
