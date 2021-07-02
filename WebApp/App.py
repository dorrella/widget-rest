import tornado.ioloop
import tornado.web
from .Database import init_db

# list handlers individually to make pep8 happy
from .Nodes import WidgetHandler
from .Nodes import WidgetEntryHandler


class WebApp(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(WebApp, self).__init__(*args, **kwargs)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    path_handlers = [
        (r"/", MainHandler),
        (r"/widget/?", WidgetHandler),
        (r"/widget/\d*/?", WidgetEntryHandler),
    ]

    app = WebApp(path_handlers)

    return app


def make_test_app():
    app = make_app()
    # init db
    # todo in memory sql for this only
    init_db()

    return app


def run_app(port):
    # todo check that port is a valid int
    app = make_app()
    init_db()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
