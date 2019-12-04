import sqlite3


class Back(object):
    def __init__(self):
        db = sqlite3.connect("ski.db")
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS trip(id INTEGER PRIMARY KEY, f_name TEXT, l_name TEXT, email TEXT)")
        db.commit()
        db.close()

    def view_customer(self):
        db = sqlite3.connect("ski.db")
        cur = db.cursor()
        cur.execute("SELECT * FROM trip")
        data = cur.fetchall()
        db.close()
        return data

    def suscribe(self, name="", lastname="", email=""):
        db = sqlite3.connect("ski.db")
        cur = db.cursor()
        cur.execute("INSERT INTO trip VALUES(NULL, ?, ?, ?)", (name, lastname, email))
        db.commit()
        db.close()

if __name__=="__main__":
    bk = Back()
    db = sqlite3.connect("ski.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM trip")
    data = cur.fetchall()
    for line in data:
        print(line)
    db.close()
