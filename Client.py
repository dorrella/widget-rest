#!/usr/bin/env python3

import requests

host = "localhost"
port = 8080
path = "widget"

url = f"http://{host}:{port}/{path}"

response = requests.get(url)
data = response.json()
print(data)

with open("json/test1.json", "r") as f:
    text = f.read()

response = requests.post(url, data=text)
data = response.json()
print(data)
