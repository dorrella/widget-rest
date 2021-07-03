import json

from .Main_test import TestMainHandlerSetup, json_path, load_json


class TestWidgetHandler(TestMainHandlerSetup):
    """WidgetHandler unit tests"""

    def test_get(self):
        """test list"""
        response = self.fetch("/widget")
        self.assertEqual(response.code, 200)

        response = self.fetch("/widget/")
        self.assertEqual(response.code, 200)

    def test_post(self):
        """test create"""
        test_json = json_path / "test1.json"
        good_name = json_path / "widget_good_name.json"
        bad_name = json_path / "widget_bad_name.json"
        bad_parts = json_path / "widget_bad_parts.json"

        # check it creates with the correct data
        body = load_json(test_json)
        response = self.fetch("/widget", method="POST", body=body)
        data = json.loads(response.body)
        self.assertEqual(response.code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "test")
        self.assertEqual(data["parts"], 10)

        # check input validation

        # name is exactly 64
        body = load_json(good_name)
        response = self.fetch("/widget", method="POST", body=body)
        self.assertEqual(response.code, 200)

        # name must be < 64
        body = load_json(bad_name)
        response = self.fetch("/widget", method="POST", body=body)
        self.assertEqual(response.code, 400)

        # for this just check substring of err message
        correct_msg = False
        msg = response.body.decode("utf8")
        if "too long" in msg:
            correct_msg = True
        self.assertTrue(correct_msg)

        # parts must be int
        body = load_json(bad_parts)
        response = self.fetch("/widget", method="POST", body=body)
        self.assertEqual(response.code, 400)
        self.assertEqual(response.body, b"parts: ten must be integer")
