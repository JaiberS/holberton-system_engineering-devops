#!/usr/bin/python3
"""  For a given employee ID, returns information """
import requests
from sys import argv
import json

if __name__ == "__main__":
    """ Get information """
    str0 = "https://jsonplaceholder.typicode.com/"
    user_tasks = requests.get(str0 + "todos",
                              params={"userId": argv[1]})
    user = requests.get(str0 + "users/" + argv[1])
    to_json1 = []
    to_json = {}
    for i in user_tasks.json():
        to_json2 = {}
        to_json2.setdefault("task", i["title"])
        to_json2.setdefault("completed", i["completed"])
        to_json2.setdefault("username", user.json()["name"])
        to_json1.append(to_json2)
    to_json.setdefault(argv[1], to_json1)
    with open(argv[1] + ".json", "w") as save:
        json.dump(to_json, save)
