import logging
from http.server import HTTPServer

import routes
from rest_request_handler.rest_request_handler import RestRequestHandler


HOST = "127.0.0.1"
PORT = 5000

logging.basicConfig(format=f"[i] {HOST}:{PORT} -> %(asctime)s: %(message)s")

server = HTTPServer((HOST, PORT), RestRequestHandler)



# print(RestRequestHandler.get_PathMap)
try:
    print(f"Server started at: http://{HOST}:{PORT}")
    server.serve_forever()
    
except KeyboardInterrupt:
    print("Server stoped!")

