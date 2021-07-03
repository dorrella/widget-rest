import unittest
import json

from .Main_test import json_path
from WebApp.Endpoints.Widget.Widget import Widget

date = "2021-07-01"


class TestWidget(unittest.TestCase):
    """test for Widget class"""

    def test_from_json(self):
        """tests json parsing"""
        w = Widget()
        path = json_path / "test1.json"
        with open(path, "r") as f:
            text = f.read()
        w.from_json(text)
        self.assertIsNone(w.id)
        self.assertIsNone(w.updated)
        self.assertIsNone(w.created)
        self.assertEqual(w.name, "test")
        self.assertEqual(w.parts, 10)

    def test_to_json(self):
        """tests json dumping"""
        w = Widget()
        w.id = 1
        w.name = "test"
        w.parts = 10
        w.created = date
        w.updated = date
        text = w.to_json()
        data = json.loads(text)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "test")
        self.assertEqual(data["parts"], 10)
        self.assertEqual(data["updated"], date)
        self.assertEqual(data["created"], date)

    def test_from_dict(self):
        """test loading from dict"""
        w = Widget()
        data = {
            "id": 1,
            "name": "test",
            "parts": 10,
            "created": date,
            "updated": date,
        }
        w.from_dict(data)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "test")
        self.assertEqual(data["parts"], 10)
        self.assertEqual(data["updated"], date)
        self.assertEqual(data["created"], date)

    def test_to_dict(self):
        """tests dumping to dict"""
        w = Widget()
        w.id = 1
        w.name = "test"
        w.parts = 10
        w.created = date
        w.updated = date
        data = w.to_dict()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "test")
        self.assertEqual(data["parts"], 10)
        self.assertEqual(data["updated"], date)
        self.assertEqual(data["created"], date)

    def test_eq(self):
        """tests comparision with __eq__"""
        w = Widget()
        other = Widget()
        w.id = 1
        other.id = 1
        w.parts = 10
        other.parts = 10
        w.created = date
        other.created = date
        w.updated = date
        other.updated = date
        self.assertTrue(w == other)

        # failures
        other.id = 2
        self.assertFalse(w == other)
        other.id = w.id
        other.parts = 5
        self.assertFalse(w == other)
        other.parts = w.parts
        other.created = "bad-date"
        self.assertFalse(w == other)
        other.created = w.created
        other.updated = "bad-date"
        self.assertFalse(w == other)
        other.updated = w.updated

        # just to double check
        self.assertTrue(w == other)
