import os
from pathlib import Path
from tornado.testing import AsyncHTTPTestCase

from WebApp.App import make_test_app

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
json_path = dir_path / "../../json"


class TestMainHandlerSetup(AsyncHTTPTestCase):
    """dummy template that makes a test app and will
    populate it on request"""

    def get_app(self):
        app = make_test_app()
        return app

    def populate_db(self):
        """adds 3 widgets to the db for testing. note
        that each tests starts with an empty database"""
        for file_path in ["test1", "test2", "test3"]:
            path = json_path / f"{file_path}.json"
            with open(path, "r") as f:
                text = f.read()
            self.fetch("/widget", method="POST", body=text)
