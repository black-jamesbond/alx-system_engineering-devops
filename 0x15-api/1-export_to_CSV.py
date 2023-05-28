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
    user_name = users_data.get('username')
    ids = users_data.get('id')
    completed_status = []
    task_title = []
    for i in todo_list:
        if i.get('userId') == id:
            completed_status.append(i.get("completed"))
            task_title.append(i.get("title"))
                
    file_name = "{}.csv".format(id)
    with open (file_name,"w") as file:
        for i in range(len(task_title)):
            file.write("'{}','{}','{}','{}'\n".format(ids,user_name,completed_status[i],task_title[i]))