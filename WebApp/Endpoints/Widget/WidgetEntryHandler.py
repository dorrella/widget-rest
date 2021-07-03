import json

from .Widget import get_widget
from ..Template import TemplateHandler, get_datestamp
from ...Database import get_db, commit_db

# is this the best place for these
update_str = """
update widget
    set name = ? ,
        parts = ? ,
        updated = ?
    where id = ?
"""

del_str = """
delete from widget
    where id = ?
"""


class WidgetEntryHandler(TemplateHandler):
    def get(self):
        tokens = self.request.path.split("/")

        # primary key  is the third token
        id = tokens[2]
        if id == "":
            msg = f"bad path {self.request.path}"
            self.err_out(404, msg)
            return

        try:
            widget = get_widget(id)
        except:
            msg = f"bad path {self.request.path}"
            self.err_out(404, msg)
            return
        data = widget.to_json()
        self.write(data)

    def put(self):
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
            self.err_out(400, "bad input")
            return

        # validate input
        if len(name) > 64:
            msg = f"name: {name} too long"
            self.err_out(400, msg)
            return

        if not isinstance(parts, int):
            msg = f"parts: {parts} must be integer"
            self.err_out(400, msg)
            return

        # find current widget
        try:
            w = get_widget(id)
        except:
            msg = f"could not find widget by id {id}"
            self.err_out(404, msg)
            return

        ds = get_datestamp()
        w.parts = parts
        w.name = name
        w.updated = ds

        db = get_db()
        try:
            db.execute(update_str, (name, parts, ds, id))
            commit_db()
        except:
            self.err_out(500, "internal server error")
            return

        self.write(w.to_json())

    def delete(self):
        tokens = self.request.path.split("/")
        id = tokens[2]
        db = get_db()

        try:
            db.execute(del_str, (id))
            commit_db()
        except:
            self.err_out(500, "internal server error")
            return

        self.set_status(204)
