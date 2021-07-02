import json

from ...Database import get_db


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
        data = self.to_dict()
        data_str = json.dumps(data)
        return data_str

    def from_json(self, j):
        # maybe we should check this is a dict
        d = json.loads(j)
        self.from_dict(d)

    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "parts": self.parts,
            "created": self.created,
            "updated": self.updated,
        }
        return data

    def from_dict(self, d):
        # this can throw errors, but i think
        # we want to handle them down the stack
        self.id = d["id"]
        self.name = d["name"]
        self.parts = d["parts"]
        self.created = d["created"]
        self.updated = d["updated"]
