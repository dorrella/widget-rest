#!/usr/bin/env python3

import requests

from WebApp.Endpoints.Widget.Widget import Widget

host = "localhost"
port = 8080
path = "widget"

url = f"http://{host}:{port}/{path}"


def print_widget(w):
    print(f"  name: {w.name}")
    print(f"    id     : {w.id}")
    print(f"    parts  : {w.parts}")
    print(f"    created: {w.created}")
    print(f"    updated: {w.updated}")


# get all widgets
response = requests.get(url)
data = response.json()

widgets = []
print("widgets")
for d in data:
    w = Widget()
    w.from_dict(d)
    print_widget(w)
    widgets.append(w)

print("delete old widgets")
for w in widgets:
    response = requests.delete(f"{url}/{w.id}")

print("adding new widgets")
for path in ["test1", "test2", "test3"]:
    with open(f"json/{path}.json", "r") as f:
        text = f.read()

    response = requests.post(url, data=text)
    data = response.json()
    w = Widget()
    w.from_dict(data)
    print_widget(w)


print(f"updating widget {w.id}")
w.name = "gandalf"
data = w.to_json()
response = requests.put(f"{url}/{w.id}", data=data)
data = response.json()
w = Widget()
w.from_dict(data)
print_widget(w)

print(f"getting widget {w.id}")
response = requests.get(f"{url}/{w.id}")
data = response.json()
w = Widget()
w.from_dict(data)
print_widget(w)
