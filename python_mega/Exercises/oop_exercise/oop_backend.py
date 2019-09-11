import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def view_all(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def search_entry(self, title='', author='', year='', isbn=''):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                    (title, author, year, isbn))
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def add_entry(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",
                    (title, author, year, isbn))
        self.conn.commit()

    def update(id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? where id=?",
                    (title, author, year, isbn, id))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()