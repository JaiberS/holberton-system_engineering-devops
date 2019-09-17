#!/usr/bin/python3
"""  For a given employee ID, returns information """
import json
import requests

if __name__ == "__main__":
    """ Get information """
    str0 = "https://jsonplaceholder.typicode.com/"
    user_tasks = requests.get(str0 + "todos/")
    user = requests.get(str0 + "users/")
    to_json = {}
    for j in user.json():
        to_json1 = []
        for i in user_tasks.json():
            if j["id"] == i["userId"]:
                to_json2 = {}
                to_json2.setdefault("task", i["title"])
                to_json2.setdefault("completed", i["completed"])
                to_json2.setdefault("username", j["name"])
                to_json1.append(to_json2)
                to_json.setdefault(j["id"], to_json1)
    with open("todo_all_employees.json", "w") as save:
        json.dump(to_json, save)
