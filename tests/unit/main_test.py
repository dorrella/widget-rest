import os
from pathlib import Path
from tornado.testing import AsyncHTTPTestCase

from WebApp.App import make_test_app

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
json_path = dir_path / "../../json"


class TestMainHandlerSetup(AsyncHTTPTestCase):
    def get_app(self):
        return make_test_app()


class TestMainHandler(TestMainHandlerSetup):
    def test_get(self):
        response = self.fetch("/")
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b"Hello, world")

        response = self.fetch("/", method="DELETE")
        self.assertEqual(response.code, 405)
