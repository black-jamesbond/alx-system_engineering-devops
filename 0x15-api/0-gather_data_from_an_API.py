#!/usr/bin/python3
"""Using https://jsonplaceholder.typicode.com returns info about employee todo progress Implemented using recursion"""

import requests
import sys

api = "https://jsonplaceholder.typicode.com/"
id = int(sys.argv[1])
"""REST API url"""
if __name__ == "__main__":
    users_data = dict(requests.get("{}users/{}".format(api, id)).json())
    todo_list = list(requests.get("{}todos".format(api)).json())
    user_name = users_data.get('name')
    todo = 0
    completed = 0
    task_title = []
    for i in todo_list:
        if i.get('userId') == id:
            todo += 1
            if i.get("completed") == True:
                completed += 1
                task_title.append(i.get("title"))
                
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_name, 
            completed, 
            todo)
    )
    for i in task_title:
        print("\t{}".format(i))