from .Main_test import TestMainHandlerSetup, json_path

# should be in some common lib


def load_json(path):
    with open(path, "r") as f:
        text = f.read()
    return text


class TestWidgetHandler(TestMainHandlerSetup):
    def test_get(self):
        response = self.fetch("/widget")
        self.assertEqual(response.code, 200)

        response = self.fetch("/widget/")
        self.assertEqual(response.code, 200)

    def test_post(self):
        test_json = json_path / "test1.json"
        bad_name = json_path / "widget_bad_name.json"
        bad_parts = json_path / "widget_bad_parts.json"

        body = load_json(test_json)
        response = self.fetch("/widget", method="POST", body=body)
        self.assertEqual(response.code, 200)

        body = load_json(bad_name)
        response = self.fetch("/widget", method="POST", body=body)
        self.assertEqual(response.code, 400)

        # for this just check substring of err message
        correct_msg = False
        msg = response.body.decode("utf8")
        if "too long" in msg:
            correct_msg = True
        self.assertTrue(correct_msg)

        body = load_json(bad_parts)
        response = self.fetch("/widget", method="POST", body=body)
        self.assertEqual(response.code, 400)
        self.assertEqual(response.body, b"parts: ten must be integer")
