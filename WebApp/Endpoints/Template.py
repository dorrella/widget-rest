import tornado.web
from datetime import date
from ..Logger import error


def get_datestamp():
    """returns datestamp for use with updates
    in the format YEAR-MONTH-DAY

    :return: string containing datestamp
    :return type: string"""
    return date.today().isoformat()


class TemplateHandler(tornado.web.RequestHandler):
    """wrapper for common handler functions"""

    def err_out(self, status, tf, message):
        """clear outstream, sets http status,
        and writes message out

        :param status: http status
        :type status: int
        :param tf: trace flag for error message
        :type tf: WebApp.Logger.TraceFlag
        :param message: message to return
        :type message: string"""
        error(tf, message)

        self.clear()
        self.set_status(status)
        self.finish(message)
