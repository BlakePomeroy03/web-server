import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = '127.0.0.1'
PORT = 8080

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Listening on " + HOST + ":" + str(PORT))

client_connection, client_address = server_socket.accept()
print("Connection from: " + str(client_address))

raw_bytes = client_connection.recv(1024)

request_data = raw_bytes.decode('utf-8', errors='replace')

print("\n--- INCOMING MESSAGE ---")
print(request_data)
print("------------------------\n")

client_connection.close()
print("Connection closed")