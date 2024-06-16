import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS expense_table (item_name TEXT, item_price FLOAT, purchase_date DATE)"
        )
        self.conn.commit()

    def fetchRecord(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insertRecord(self, item_name, item_price, purchase_date):
        self.cur.execute("INSERT INTO expense_table VALUES (?, ?, ?)", (item_name, item_price, purchase_date))
        self.conn.commit()

    def removeRecord(self, rwid):
        self.cur.execute("DELETE FROM expense_table WHERE rowid=?", (rwid,))
        self.conn.commit()

    def updateRecord(self, item_name, item_price, purchase_date, rid):
        self.cur.execute(
            "UPDATE expense_table SET item_name=?, item_price=?, purchase_date=? WHERE rowid=?",
            (item_name, item_price, purchase_date, rid)
        )
        self.conn.commit()

    def __del__(self):
        self.conn.close()
