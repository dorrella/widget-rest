import json

from ...Database import get_db

# list all widgets from database


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


# get single widget
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


# wrapper around widget data
class Widget:
    def __init__(self):
        self.id = None
        self.name = None
        self.parts = None
        self.created = None
        self.updated = None

    def __eq__(self, other):
        if not isinstance(other, Widget):
            return False
        if self.id != other.id:
            return False
        if self.parts != other.parts:
            return False
        if self.updated != other.created:
            return False
        if self.updated != other.updated:
            return False
        return True

    # convert to json string
    def to_json(self):
        data = self.to_dict()
        data_str = json.dumps(data)
        return data_str

    # convert from json string
    def from_json(self, j):
        # maybe we should check this is a dict
        d = json.loads(j)
        self.from_dict(d)

    # convert to dictionary
    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "parts": self.parts,
            "created": self.created,
            "updated": self.updated,
        }
        return data

    # convert from dictionary
    def from_dict(self, d):
        if "id" in d:
            self.id = d["id"]
        if "created" in d:
            self.created = d["created"]
        if "updated" in d:
            self.updated = d["updated"]

        self.name = d["name"]
        self.parts = d["parts"]
