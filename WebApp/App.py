import tornado.ioloop
import tornado.web

from .Logger import init_logger, TraceFlag, info
from .Database import init_db, init_test_db

# list handlers individually to make pep8 happy
from .Endpoints import MainHandler
from .Endpoints import WidgetHandler
from .Endpoints import WidgetEntryHandler


def make_app():
    """creates test app for tests

    :return: tornado app for testing"""
    path_handlers = [
        (r"/", MainHandler),
        (r"/widget/?", WidgetHandler),
        (r"/widget/\d*/?", WidgetEntryHandler),
    ]

    app = tornado.web.Application(path_handlers)

    return app


def make_test_app():
    """creates test app for tests using
    in memory database

    :return: tornado app for testing"""
    init_logger("test_log.txt", False)
    app = make_app()
    init_test_db()
    return app


def run_app(port, database, logfile):
    """starts web app and waits for Ctrl+C interrupt

    :param port: port to run the app on
    :type port: int
    :param database: path to database
    :type database: string
    :param logfile: path to log
    :type logfile: string"""

    init_logger(logfile, True)
    info(TraceFlag.APP, "initializing app")

    app = make_app()
    init_db(database)
    app.listen(port)

    info(TraceFlag.APP, "starting server")
    try:
        tornado.ioloop.IOLoop.current().start()
    except:
        tornado.ioloop.IOLoop.instance().stop()
