import sqlite3


class Back(object):
    def __init__(self):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS movie_table (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, director TEXT, lead TEXT)")
        db.commit()
        db.close()

    def view_all(self):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("SELECT * FROM movie_table")
        data = cur.fetchall()
        db.close()
        return data

    def add_element(self, title="", year=2012, director="Johnny Derp", lead="Brad Pitt"):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("INSERT INTO movie_table VALUES(NULL, ?, ?, ?, ?)", (title, year, director, lead))
        db.commit()
        db.close()

    def del_element(self, id):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("DELETE FROM movie_table WHERE id=?", (id,))
        db.commit()
        db.close()

    def update_element(self, id, title="", year=2012, director="Johnny Derp", lead="Brad Pitt"):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("UPDATE movie_table SET title=?, year=?, director=?, lead=?, WHERE id=?", (title, year, director, lead, id))
        db.commit()
        db.close()

# debug database
if __name__ == "__main__":
    bk = Back()
    db = sqlite3.connect("movies.db")
    cur = db.cursor()
    cur.execute("INSERT INTO movie_table VALUES(NULL, ?, ?, ?, ?)", ("Finding Nemo", 2003, "Andre Stanton", "Dory"))
    db.commit()
    cur.execute("SELECT * FROM movie_table")
    data = cur.fetchall()
    for line in data:
        print(line)
    db.close()