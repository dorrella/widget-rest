import json

from .Widget import Widget, get_all_widgets
from .Constants import insert_str
from ..Template import TemplateHandler, get_datestamp
from ...Database import get_db, commit_db
from ...Logger import TraceFlag, info, debug


class WidgetHandler(TemplateHandler):
    """Handler for /widget"""

    def get(self):
        """list endpoint for /widget"""
        debug(TraceFlag.WIDGET, "list request for widget")
        widgets = get_all_widgets()
        # would be faster to do this inline in get_all_widgets,
        # but maybe it's better to have the Object?
        data = []
        for w in widgets:
            data.append(w.to_dict())
        data_str = json.dumps(data)
        self.write(data_str)

    def post(self):
        """create endpoint for /widget"""
        info(TraceFlag.WIDGET, "create request for widget")
        msg = f"update request for widget:{self.request.body}"
        debug(TraceFlag.WIDGET, msg)

        try:
            data = json.loads(self.request.body)
            name = data["name"]
            parts = data["parts"]
        except:
            self.err_out(400, TraceFlag.WIDGET, "bad input")
            return

        # validate input
        # name must be <= 64 chars
        if len(name) > 64:
            msg = f"name: {name} too long"
            self.err_out(400, TraceFlag.WIDGET, msg)
            return

        # parts must be int
        if not isinstance(parts, int):
            msg = f"parts: {parts} must be integer"
            self.err_out(400, TraceFlag.WIDGET, msg)
            return

        ds = get_datestamp()
        w = Widget()
        w.name = name
        w.parts = parts
        w.created = ds
        w.updated = ds

        # try/except?
        db = get_db()
        db.execute(insert_str, (name, parts, ds, ds))
        commit_db()

        # not sure if these are guarenteed to be the same
        w.id = db.lastrowid
        self.write(w.to_json())
