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


def get_widget(id):
    query = "select * from widget where id=?"
    db = get_db()
    db.execute(query, (id))
    rows = db.fetchall()

    if len(rows) != 1:
        raise ("unexpected number of results")

    id, name, parts, created, updated = rows[0]
    w = Widget()
    w.id = id
    w.name = name
    w.parts = parts
    w.created = created
    w.updated = updated
    return w


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
        tokens = self.request.path.split("/")
        num_tokens = len(tokens)

        if num_tokens == 2:
            self.all_widgets()

        elif num_tokens == 3:
            # primary key  is the third token
            id = tokens[2]
            if id == "":
                # handle case with path is /widget/
                self.all_widgets()
            else:
                self.get_widget(id)
        else:
            self.clear()
            self.set_status(404)
            self.finish("unknown error")

    def all_widgets(self):
        widgets = get_all_widgets()
        # would be faster to do this inline in get_all_widgets,
        # but maybe it's better to have the Object?
        data = []
        for w in widgets:
            data.append(w.to_json())
            data_str = json.dumps(data)
            self.write(data_str)

    def get_widget(self, id):
        try:
            widget = get_widget(id)
        except:
            self.clear()
            self.set_status(400)
            self.finish("unknown error")
        # would be faster to do this inline in get_all_widgets,
        # but maybe it's better to have the Object?
        data = widget.to_json()
        self.write(data)
