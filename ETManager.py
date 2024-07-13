import sqlite3
import os


con = sqlite3.connect("expensetracker.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Expense (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT,
    receipt_photo BLOB
)
""")
res = cur.execute("SELECT name FROM sqlite_master")
table_name = res.fetchone()
print(table_name)

data = [
    ("13-07-2024","Jaga", float(3100), "Debt","", "",float(0),"")
]