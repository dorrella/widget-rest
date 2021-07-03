import json

from .Main_test import TestMainHandlerSetup, json_path
from WebApp.Nodes.Template import get_datestamp

# should be in some common lib


def load_json(path):
    with open(path, "r") as f:
        text = f.read()
    return text


class TestWidgetHandler(TestMainHandlerSetup):
    def test_get(self):
        # db starts empty
        response = self.fetch("/widget/1")
        self.assertEqual(response.code, 404)

        # add ids 1 2 and 3
        self.populate_db()
        # has to match today
        date = get_datestamp()

        # try again
        response = self.fetch("/widget/1")
        self.assertEqual(response.code, 200)
        data = json.loads(response.body.decode("utf8"))
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "test")
        self.assertEqual(data["parts"], 10)
        self.assertEqual(data["updated"], date)
        self.assertEqual(data["created"], date)

    def test_delete(self):
        # db starts empty
        # add ids 1 2 and 3
        self.populate_db()
        response = self.fetch("/widget/1", method="DELETE")
        self.assertEqual(response.code, 204)

    def test_put(self):
        # db starts empty
        data = {"name": "gandalf", "parts": 5}
        text = json.dumps(data)
        response = self.fetch("/widget/1", method="PUT", body=text)
        self.assertEqual(response.code, 404)

        # add ids 1 2 and 3
        self.populate_db()

        response = self.fetch("/widget/1", method="PUT", body=text)
        self.assertEqual(response.code, 200)
        data2 = json.loads(response.body.decode("utf8"))
        self.assertEqual(data["name"], data2["name"])
        self.assertEqual(data["parts"], data2["parts"])

        bad_name = json_path / "widget_bad_name.json"
        bad_parts = json_path / "widget_bad_parts.json"

        body = load_json(bad_name)
        response = self.fetch("/widget/1", method="PUT", body=body)
        self.assertEqual(response.code, 400)

        body = load_json(bad_parts)
        response = self.fetch("/widget/1", method="PUT", body=body)
        self.assertEqual(response.code, 400)
