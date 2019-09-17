#!/usr/bin/python3
"""  For a given employee ID, returns information """
import csv
import requests
from sys import argv

if __name__ == "__main__":
    """ Get information """
    str0 = "https://jsonplaceholder.typicode.com/"
    user_tasks = requests.get(str0 + "todos",
                              params={"userId": argv[1]})
    user = requests.get(str0 + "users/" + argv[1])
    with open(argv[1] + ".csv", "w") as csv0:
        csv0_info = csv.writer(csv0, quoting=csv.QUOTE_ALL)
        for i in user_tasks.json():
            csv0_info.writerow([i["userId"], user.json()["username"],
                                i["completed"], i["title"]])
