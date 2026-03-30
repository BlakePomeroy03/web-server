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

request_data = client_connection.recv(1024).decode('utf-8')
print("Received request:")
print(request_data)

client_connection.close()
print("Connection closed")
