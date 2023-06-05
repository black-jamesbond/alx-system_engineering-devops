#!/usr/bin/python3
"""Using https://jsonplaceholder.typicode.com returns info about employee todo progress Implemented using recursion"""
import json
import requests
import sys

api = "https://jsonplaceholder.typicode.com/"
id = int(sys.argv[1])
"""REST API url"""
if __name__ == "__main__":
    value = []
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
                
    file_name = "{}.json".format(id)
    with open (file_name,"w+") as file:
        _dict = {'{}'.format(ids):value}
        
        for i in range(len(task_title)):
            dic_value = {"username": user_name,
                         "task": task_title[i],
                         "completed": completed_status[i]}
            value.append(dic_value)
        json.dump(_dict, file)