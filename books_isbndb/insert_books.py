import json
import sqlite3

# Open JSON
with open("books_children.json", "r", encoding="utf-8") as f:
    books = json.load(f)

# Conect to db
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Insert books
for book in books:
    title = book.get("title")
    image = book.get("image")
    authors = ", ".join(book.get("authors", []))
    # command that send the SQL instruction to DB ? as a placeholder to protect SQL injection
    cursor.execute("""
        INSERT INTO books (title, image, authors)
        VALUES (?, ?, ?)
    """, (title, image, authors))

conn.commit()
conn.close()