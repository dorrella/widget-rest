import sqlite3

create_str = """
create table widget (
    id INTEGER PRIMARY KEY,
    name TEXT,
    parts INTEGER,
    created TEXT,
    updated TEXT)
"""
insert_str = """
insert into widget
    (name, parts, created, updated)
    values (?, ?, ?, ?)
"""


def init_db():
    global db
    db = Database()
    db.populate()


def get_db():
    return db.con.cursor()


class Database:
    def __init__(self):
        self.con = sqlite3.connect(":memory:")

    def populate(self):
        cur = self.con.cursor()
        cur.execute(create_str)
        widgets = [
            ("foo", 1, "2020-03-21", "2020-10-03"),
            ("bar", 1, "2021-09-15", "2021-09-15"),
        ]
        cur.executemany(insert_str, widgets)
