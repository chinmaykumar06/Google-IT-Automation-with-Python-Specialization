#!/usr/bin/env python3

import os
import requests

#Path to the data
path = "/data/feedback"

keys = ["title", "name", "date", "feedback"]

folder = os.listdr(path)
for file in folder:
    key_count = 0
    feedback = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            feedback[keys[key_count]] = value
            key_count += 1
    print(feedback)
    reponse = requests.post("http://35.255.144.156/feedback/",json=feedback)
print(response.request.body)
print(response.status_code)