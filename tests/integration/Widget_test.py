import json

from .Common_test import TestMainHandlerSetup
from WebApp.Endpoints.Widget.Widget import Widget


def load_json(path):
    """helper to load json inline"""
    with open(path, "r") as f:
        text = f.read()
    return text


class TestWidgetHandler(TestMainHandlerSetup):
    """integration and regression tests for the Widget
    Endpoints. Mostly makes sure that the different endpoints
    are working together. Far from exhaustive"""

    def test_get(self):
        """test to check contest of list are equal to contents of get"""
        self.populate_db()
        w = Widget()

        response = self.fetch("/widget")
        self.assertEqual(response.code, 200)

        data = json.loads(response.body)
        for d in data:
            w.from_dict(d)
            other = Widget()
            response = self.fetch(f"/widget/{w.id}")
            other.from_json(response.body)
            self.assertEqual(response.code, 200)
            self.assertTrue(w == other)

    def test_update(self):
        """test that an update will update the
        correct fields.

        todo need a way to monkey patch the created/updated
        dates"""
        self.populate_db()
        w = Widget()

        response = self.fetch("/widget/1")
        self.assertEqual(response.code, 200)
        w.from_json(response.body)

        data = {"name": "gandalf", "parts": 5}
        text = json.dumps(data)
        response = self.fetch("/widget/1", method="PUT", body=text)
        self.assertEqual(response.code, 200)

        other = Widget()
        other.from_json(response.body)
        self.assertFalse(w == other)
        self.assertNotEqual(other.name, w.name)
        self.assertNotEqual(other.parts, w.parts)

    def test_delete(self):
        """test we can delete widgets"""
        # test not there
        response = self.fetch("/widget/1")
        self.assertEqual(response.code, 404)

        # add id 1 and try again
        self.populate_db()
        response = self.fetch("/widget/1")
        self.assertEqual(response.code, 200)

        # delete
        response = self.fetch("/widget/1", method="DELETE")
        self.assertEqual(response.code, 204)

        # tests it's gone
        response = self.fetch("/widget/1")
        self.assertEqual(response.code, 404)
