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
    raw_bytes = client_connection.recv(1024)
    request_data = raw_bytes.decode('utf-8', errors='replace')
    
    if not request_data:
        client_connection.close()
        continue

    request_lines = request_data.split('\r\n')
    first_line = request_lines[0]
    
    try:
        method, path, version = first_line.split(' ')
    except ValueError:
        client_connection.close()
        continue
        
    print("User requested path: " + path)

    if path == '/':
        status = "HTTP/1.1 200 OK\r\n"
        body = "<html><body><h1>Home Page</h1><p>Welcome to the main dashboard.</p></body></html>"
    elif path == '/about':
        status = "HTTP/1.1 200 OK\r\n"
        body = "<html><body><h1>About Me</h1><p>I built this server from scratch.</p></body></html>"
    else:
        status = "HTTP/1.1 404 Not Found\r\n"
        body = "<html><body><h1>404 Error</h1><p>That page does not exist on this server.</p></body></html>"

    http_response = status + "Content-Type: text/html\r\n\r\n" + body
    
    client_connection.sendall(http_response.encode('utf-8'))
    client_connection.close()