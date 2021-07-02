from WebApp.App import make_test_app
from tornado.testing import AsyncHTTPTestCase


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
