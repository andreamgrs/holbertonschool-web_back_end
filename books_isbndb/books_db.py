import sqlite3

# Create or connect to the DB
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Create table
cursor.execute("""CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    image TEXT,
    authors TEXT
)""")

conn.commit()
conn.close()