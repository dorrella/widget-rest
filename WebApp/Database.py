import sqlite3

create_str = """
create table if not exists widget (
    id integer primary key,
    name text,
    parts integer,
    created text,
    updated text)
"""


def init_test_db():
    global db
    db = Database(None)
    db.populate()


def init_db(file):
    global db
    db = Database(file)
    db.populate()


def get_db():
    return db.con.cursor()


class Database:
    def __init__(self, file):
        if file is None:
            self.con = sqlite3.connect(":memory:")
            return
        self.con = sqlite3.connect(file)

    def populate(self):
        cur = self.con.cursor()
        cur.execute(create_str)
