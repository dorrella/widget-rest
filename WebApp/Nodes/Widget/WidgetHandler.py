import json
from datetime import date

from .Widget import Widget, get_all_widgets
from ..Template import TemplateHandler
from ...Database import get_db, commit_db

insert_str = """
insert into widget
    (name, parts, created, updated)
    values (?, ?, ?, ?)
"""

# should probably be in some common place


def get_datestamp():
    return date.today().isoformat()


class WidgetHandler(TemplateHandler):
    def get(self):
        widgets = get_all_widgets()
        # would be faster to do this inline in get_all_widgets,
        # but maybe it's better to have the Object?
        data = []
        for w in widgets:
            data.append(w.to_dict())
        data_str = json.dumps(data)
        self.write(data_str)

    def post(self):
        # ignore path errors, for now
        try:
            data = json.loads(self.request.body)
            name = data["name"]
            parts = data["parts"]
        except:
            self.err_out(400, "unknown error")
            return

        if len(name) > 64:
            msg = f"name: {name} too long"
            self.err_out(400, msg)
            return

        if not isinstance(parts, int):
            msg = f"parts: {parts} must be integer"
            self.err_out(400, msg)
            return

        ds = get_datestamp()
        w = Widget()
        w.name = name
        w.parts = parts
        w.created = ds
        w.updated = ds

        db = get_db()
        db.execute(insert_str, (name, parts, ds, ds))
        commit_db()
        # not sure if these are guarenteed to be the same
        w.id = db.lastrowid
        self.write(w.to_json())
