import logging
from http.server import ThreadingHTTPServer

from .routes import *
from .rest_request_handler import RestRequestHandler



def run(host: str="127.0.0.1", port: int=8081, keyIntHandle: bool=True, msg: bool=True):
    server = ThreadingHTTPServer((host, port), RestRequestHandler)
    
    if msg: logging.info(f"RestServer -> started at: http://{host}:{port}")
    if keyIntHandle:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            if msg: logging.info("RestServer -> stoped!")
    else:
        server.serve_forever()

def get_configured_server(host: str="127.0.0.1", port: int=8081) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), RestRequestHandler)

if __name__ == "__main__":
    run()