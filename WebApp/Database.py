import sqlite3

from .Logger import TraceFlag, info, debug

# string to populate widget table
# for more complex apps, put in a list
# with one entry per table, and then have
# db.populate() iterate over it
create_str = """
create table if not exists widget (
    id integer primary key,
    name text,
    parts integer,
    created text,
    updated text)
"""


def init_test_db():
    """initialize the in memory
    db singleton for tests"""
    msg = "initializing test database"
    info(TraceFlag.DB, msg)
    global db
    db = Database(None)
    db.populate()


def init_db(file):
    """initialize the db singleton"""
    global db
    msg = f"initializing database {file}"
    info(TraceFlag.DB, msg)
    db = Database(file)
    db.populate()


def get_db():
    """gets a curser to the database

    :return: cursor to be used for database operations"""
    return db.con.cursor()


def commit_db():
    """commits changes to database"""
    debug(TraceFlag.DB, "commiting database")
    db.con.commit()


class Database:
    """wrapper for database singleton using sqlite3,
    creating it if it's not present

    :param file: path to sqlite database file
    :type file: string"""

    def __init__(self, file):
        if file is None:
            self.con = sqlite3.connect(":memory:")
        else:
            self.con = sqlite3.connect(file)

    def populate(self):
        """populate tables.

        if we add tables, the iterate
        over a list of cration strings"""
        cur = self.con.cursor()
        cur.execute(create_str)
