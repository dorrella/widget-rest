import tornado.ioloop
import tornado.web

from .Logger import init_logger, log_info
from .Database import init_db, init_test_db

# list handlers individually to make pep8 happy
from .Endpoints import WidgetHandler
from .Endpoints import WidgetEntryHandler


# handles / path
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    path_handlers = [
        (r"/", MainHandler),
        (r"/widget/?", WidgetHandler),
        (r"/widget/\d*/?", WidgetEntryHandler),
    ]

    app = tornado.web.Application(path_handlers)

    return app


# app just for tests
# it uses in memory database
def make_test_app():
    init_logger(None, False)
    app = make_app()
    init_test_db()
    return app


# run app
def run_app(port, database, logfile):
    init_logger(logfile, True)
    log_info("initializing app")
    app = make_app()
    log_info(f"initializing database {database}")
    init_db(database)
    app.listen(port)
    log_info("starting server")
    try:
        tornado.ioloop.IOLoop.current().start()
    except:
        tornado.ioloop.IOLoop.instance().stop()
