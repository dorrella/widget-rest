import tornado.ioloop
import tornado.web
from .Database import init_db
from .Widget import WidgetHandler

class WebApp(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(WebApp, self).__init__(*args, **kwargs)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    path_handlers = [
        (r"/", MainHandler),
        (r"/widget", WidgetHandler),
    ]

    app = WebApp(path_handlers)

    #init db
    init_db()


    return app

def run_app(port):
    #todo check that port is a valid int
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
