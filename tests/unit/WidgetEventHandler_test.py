import json

from .Main_test import TestMainHandlerSetup, json_path, load_json
from WebApp.Endpoints.Template import get_datestamp


class TestWidgetEventHandler(TestMainHandlerSetup):
    """test for WidgetEventHandler"""

    def test_get(self):
        """test read"""
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
        data = json.loads(response.body)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "test")
        self.assertEqual(data["parts"], 10)
        self.assertEqual(data["updated"], date)
        self.assertEqual(data["created"], date)

    def test_delete(self):
        """test delete"""
        # db starts empty
        # add ids 1 2 and 3
        self.populate_db()
        response = self.fetch("/widget/1", method="DELETE")
        self.assertEqual(response.code, 204)

    def test_put(self):
        """test update"""
        good_name = json_path / "widget_bad_name.json"
        bad_name = json_path / "widget_bad_name.json"
        bad_parts = json_path / "widget_bad_parts.json"

        # db starts empty, so check bad id
        data = {"name": "gandalf", "parts": 5}
        text = json.dumps(data)
        response = self.fetch("/widget/1", method="PUT", body=text)
        self.assertEqual(response.code, 404)

        # add ids 1 2 and 3
        self.populate_db()

        # check updaztes are correct
        response = self.fetch("/widget/1", method="PUT", body=text)
        self.assertEqual(response.code, 200)
        data2 = json.loads(response.body)
        self.assertEqual(data["name"], data2["name"])
        self.assertEqual(data["parts"], data2["parts"])

        # validate input

        # test max name length
        body = load_json(good_name)
        response = self.fetch("/widget/1", method="PUT", body=text)
        self.assertEqual(response.code, 200)

        # test length > 64
        body = load_json(bad_name)
        response = self.fetch("/widget/1", method="PUT", body=body)
        self.assertEqual(response.code, 400)

        # test parts is int
        body = load_json(bad_parts)
        response = self.fetch("/widget/1", method="PUT", body=body)
        self.assertEqual(response.code, 400)
