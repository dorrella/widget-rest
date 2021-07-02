import tornado.web
from datetime import date


def get_datestamp():
    return date.today().isoformat()


class TemplateHandler(tornado.web.RequestHandler):
    def err_out(self, status, message):
        self.clear()
        self.set_status(status)
        self.finish(message)
