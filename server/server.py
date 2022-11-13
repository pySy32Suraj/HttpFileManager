import socket
from http import HTTPStatus
from http.server import HTTPServer

from rest_request_handler import RestRequestHandler



HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080
server = HTTPServer((HOST, PORT), RestRequestHandler)

try:
    print(f"Server started at: http://{HOST}:{PORT}")
    server.serve_forever()
    
except KeyboardInterrupt:
    print("Server stoped!")