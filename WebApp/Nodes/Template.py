import tornado.web


class TemplateHandler(tornado.web.RequestHandler):
    def err_out(self, status, message):
        self.clear()
        self.set_status(status)
        self.finish(message)
