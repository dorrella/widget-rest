import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """Handler for the default path. Only really
    needed for development"""

    def get(self):
        """GET for /"""
        self.write("Hello, world")
