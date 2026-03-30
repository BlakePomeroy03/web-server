import socket
import sqlite3

# --- DATABASE ---
def init_db():
    db = sqlite3.connect('warehouse.db')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS visitors (id INTEGER PRIMARY KEY, ip TEXT, path TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
    db.commit()
    db.close()

init_db()

# --- SERVER ---
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = '127.0.0.1'
PORT = 8080

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server online at " + HOST + ":" + str(PORT))

while True:
    client_connection, client_address = server_socket.accept()
    raw_bytes = client_connection.recv(1024)
    request_data = raw_bytes.decode('utf-8', errors='replace')
    
    if not request_data:
        client_connection.close()
        continue

    lines = request_data.split('\r\n')
    if len(lines) > 0:
        parts = lines[0].split(' ')
        if len(parts) > 1:
            path = parts[1]
            ip_address = str(client_address[0])
            
            db = sqlite3.connect('warehouse.db')
            cursor = db.cursor()
            cursor.execute('INSERT INTO visitors (ip, path) VALUES (?, ?)', (ip_address, path))
            db.commit()
            db.close()
            
            print("Logged visit from " + ip_address + " to " + path)

    http_response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Logging Active</h1><p>Visit recorded in the database.</p></body></html>"
    
    client_connection.sendall(http_response.encode('utf-8'))
    client_connection.close()