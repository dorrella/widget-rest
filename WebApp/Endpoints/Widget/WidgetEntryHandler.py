import json

from .Widget import get_widget
from .Constants import update_str, del_str
from ..Template import TemplateHandler, get_datestamp
from ...Database import get_db, commit_db
from ...Logger import TraceFlag, info, debug


class WidgetEntryHandler(TemplateHandler):
    """Handler for /widget/{id}"""

    def get(self):
        """read endpoint for /widget/{id}"""
        tokens = self.request.path.split("/")

        # primary key  is the third token
        id = tokens[2]
        if id == "":
            msg = f"bad path {self.request.path}"
            self.err_out(404, TraceFlag.WIDGET, msg)
            return

        info(TraceFlag.WIDGET, f"get request for widget:{id}")
        try:
            widget = get_widget(id)
        except:
            msg = f"bad get path {self.request.path}"
            self.err_out(404, TraceFlag.WIDGET, msg)
            return
        data = widget.to_json()
        self.write(data)

    def put(self):
        """update endpoint for /widget/{id}"""
        tokens = self.request.path.split("/")

        # primary key  is the third token
        id = tokens[2]
        # parse input
        # this could handle empty names/parts
        # and treat them as optional
        try:
            data = json.loads(self.request.body)
            name = data["name"]
            parts = data["parts"]
        except:
            msg = f"bad input {self.request.body}"
            self.err_out(400, TraceFlag.WIDGET, msg)
            return

        info(TraceFlag.WIDGET, f"update request for widget:{id}")
        msg = f"update request for widget:{self.request.body}"
        debug(TraceFlag.WIDGET, msg)

        # validate input
        if len(name) > 64:
            msg = f"name: {name} too long"
            self.err_out(400, TraceFlag.WIDGET, msg)
            return

        if not isinstance(parts, int):
            msg = f"parts: {parts} must be integer"
            self.err_out(400, TraceFlag.WIDGET, msg)
            return

        # find current widget
        try:
            w = get_widget(id)
        except:
            msg = f"could not find widget by id {id}"
            self.err_out(404, TraceFlag.WIDGET, msg)
            return

        ds = get_datestamp()
        w.parts = parts
        w.name = name
        w.updated = ds

        # update database
        db = get_db()
        try:
            db.execute(update_str, (name, parts, ds, id))
            commit_db()
        except:
            self.err_out(500, TraceFlag.WIDGET, "internal server error")
            return

        self.write(w.to_json())

    def delete(self):
        """delete endpoint for /widget/{id}"""
        tokens = self.request.path.split("/")
        id = tokens[2]
        db = get_db()
        info(TraceFlag.WIDGET, f"delete request for widget:{id}")
        try:
            db.execute(del_str, (id))
            commit_db()
        except:
            self.err_out(500, TraceFlag.WIDGET, "internal server error")
            return

        self.set_status(204)
