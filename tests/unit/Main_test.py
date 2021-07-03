import os
from pathlib import Path
from tornado.testing import AsyncHTTPTestCase

from WebApp.App import make_test_app

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
json_path = dir_path / "../../json"


class TestMainHandlerSetup(AsyncHTTPTestCase):
    def get_app(self):
        return make_test_app()

    def populate_db(self):
        for file_name in ["test1", "test2", "test3"]:
            path = json_path / f"{file_name}.json"
            with open(path, "r") as f:
                text = f.read()
            self.fetch("/widget", method="POST", body=text)


class TestMainHandler(TestMainHandlerSetup):
    def test_get(self):
        response = self.fetch("/")
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b"Hello, world")

        response = self.fetch("/", method="DELETE")
        self.assertEqual(response.code, 405)
