# string to insert widgets
insert_str = """
insert into widget
    (name, parts, created, updated)
    values (?, ?, ?, ?)
"""

# string to update widget
update_str = """
update widget
    set name = ? ,
        parts = ? ,
        updated = ?
    where id = ?
"""

# string to delete widget
del_str = """
delete from widget
    where id = ?
"""
