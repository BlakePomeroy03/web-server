import sqlite3

connection = sqlite3.connect('warehouse.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS visitors (id INTEGER PRIMARY KEY, ip TEXT, path TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')

connection.commit()
connection.close()

print("Database warehouse.db initialized")