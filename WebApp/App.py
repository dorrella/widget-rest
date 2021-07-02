import tornado.ioloop
import tornado.web
import logging

from .Logger import init_logger
from .Database import init_db, init_test_db

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
    init_logger(None)
    app = make_app()
    init_test_db()
    return app


def run_app(port, database, logfile):
    init_logger(logfile)
    logging.info("initializing app")
    app = make_app()
    logging.info(f"initializing database {database}")
    init_db(database)
    app.listen(port)
    logging.info("starting server")
    try:
        tornado.ioloop.IOLoop.current().start()
    except:
        tornado.ioloop.IOLoop.instance().stop()
