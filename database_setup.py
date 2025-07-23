import sqlite3

conn = sqlite3.connect('users.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);asf
''')

conn.commit()
conn.close()

print("Database and table created successfully.")