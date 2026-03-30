import sqlite3

connection = sqlite3.connect('warehouse.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM visitors')
rows = cursor.fetchall()

print("--- VISITOR LOG ---")
for row in rows:
    print(row)

connection.close()