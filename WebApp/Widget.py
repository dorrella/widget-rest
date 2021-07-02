import json
import tornado.web
from .Database import get_db


def get_all_widgets():
    rows = "select * from widget"
    db = get_db()
    rows = db.execute(rows)
    widgets = []

    for row in rows:
        id, name, parts, created, updated = row

        w = Widget()
        w.id = id
        w.name = name
        w.parts = parts
        w.created = created
        w.updated = updated

        widgets.append(w)

    return widgets


class Widget:
    def __init__(self):
        self.id = None
        self.name = None
        self.created = None
        self.updated = None

    def to_json(self):
        data = {
            "id": self.id,
            "name": self.name,
            "parts": self.parts,
            "created": self.created,
            "updated": self.updated,
        }
        data_str = json.dumps(data)
        return data_str


class WidgetHandler(tornado.web.RequestHandler):
    def get(self):
        widgets = get_all_widgets()
        # would be faster to do this inline in get_all_widgets,
        # but maybe it's better to have the Object?
        data = []
        for w in widgets:
            data.append(w.to_json())
        data_str = json.dumps(data)
        self.write(data_str)
