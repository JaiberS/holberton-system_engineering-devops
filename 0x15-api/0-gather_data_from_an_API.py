#!/usr/bin/python3
"""  For a given employee ID, returns information """
import requests
from sys import argv

if __name__ == "__main__":
    """ Get information """
    str0 = "https://jsonplaceholder.typicode.com/"
    user_tasks = requests.get(str0 + "todos",
                              params={"userId": argv[1]})
    user = requests.get(str0 + "users/" + argv[1])
    j = 0
    for i in user_tasks.json():
        if i["completed"]:
            j += 1
    str0 = "Employee " + user.json()["name"] + " is done with tasks("
    print(str0 + str(j) + "/" + str(len(user_tasks.json())) + "):")
    for i in user_tasks.json():
        if i["completed"]:
            print("\t " + i["title"])
