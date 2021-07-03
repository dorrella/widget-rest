import sqlite3

create_str = """
create table if not exists widget (
    id integer primary key,
    name text,
    parts integer,
    created text,
    updated text)
"""


# init db singleton for tests
def init_test_db():
    global db
    db = Database(None)
    db.populate()


# init db singleton
def init_db(file):
    global db
    db = Database(file)
    db.populate()


# returns db singleton
def get_db():
    return db.con.cursor()


# commits changes to db
def commit_db():
    db.con.commit()


# wrapper for singleton
class Database:
    def __init__(self, file):
        if file is None:
            self.con = sqlite3.connect(":memory:")
        else:
            self.con = sqlite3.connect(file)

    def populate(self):
        cur = self.con.cursor()
        cur.execute(create_str)
