import json

from ...Database import get_db

# Should these be a static methods on the Widget Class?


def get_all_widgets():
    """gets all entries from widget table,
    puts them into Widget objects and returns
    them.

    :return: list of widgets
    :return type: list"""
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
    """gets widget by id

    :raises Error: when not found
    :return: widget
    :return type: Widget"""
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
    """holds widget data"""

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

    def to_json(self):
        """converts widget to json string

        :return: json string containing widget
        :return type: string"""
        data = self.to_dict()
        data_str = json.dumps(data)
        return data_str

    def from_json(self, j):
        """loads json into Widget

        :param j: json string
        :type j: string"""
        # maybe we should check this is a dict
        d = json.loads(j)
        self.from_dict(d)

    # convert to dictionary
    def to_dict(self):
        """converts widget to dictionary

        :return: dictionary containing widget
        :return type: dict"""
        data = {
            "id": self.id,
            "name": self.name,
            "parts": self.parts,
            "created": self.created,
            "updated": self.updated,
        }
        return data

    def from_dict(self, d):
        """loads dictionary into Widget

        :param d: dictionary container widget field
        :type d: dict"""
        # these are not required
        if "id" in d:
            self.id = d["id"]
        if "created" in d:
            self.created = d["created"]
        if "updated" in d:
            self.updated = d["updated"]

        self.name = d["name"]
        self.parts = d["parts"]
