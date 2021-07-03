import tornado.web
from datetime import date

# returns standard timestamp for endpoints


def get_datestamp():
    return date.today().isoformat()


# Wrapper to hold err_out function
class TemplateHandler(tornado.web.RequestHandler):
    def err_out(self, status, message):
        self.clear()
        self.set_status(status)
        self.finish(message)
