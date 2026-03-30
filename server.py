import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = '127.0.0.1'
PORT = 8080

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Listening on " + HOST + ":" + str(PORT))

while True:
    client_connection, client_address = server_socket.accept()
    print("Connection from: " + str(client_address))

    raw_bytes = client_connection.recv(1024)
    request_data = raw_bytes.decode('utf-8', errors='replace')
    
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "\r\n"
        "<html><body><h1>Hello</h1><p>It actually works.</p></body></html>"
    )
    
    client_connection.sendall(http_response.encode('utf-8'))
    client_connection.close()