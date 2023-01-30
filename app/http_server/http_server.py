import os
import logging
from functools import partial
from urllib import parse
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from http.server import ThreadingHTTPServer

from util.exc_formater import format_exc
from util.headers import Headers
from util.files_system import send_file

__version__ = "v1.0"




class HttpRequestHandler(BaseHTTPRequestHandler):

    server_version = "RestRequestHandler/" + __version__


    def __init__(self, *args, dir=None, **kwds) -> None: 
        self.dir = dir
        super().__init__(*args, **kwds)

    def do_GET(self):
        try:
            path = self.get_path()
            if not os.path.isfile(path):
                raise FileNotFoundError("File not found: " + path)
            
            send_file(self, path, self.download)
        except Exception:
            Headers(self, {
                "Content-Type": "text/html"
            }).send(HTTPStatus.INTERNAL_SERVER_ERROR).end()
            
            self.wfile.write(format_exc().replace("\n", "</br>").encode("utf-8"))
            logging.error("HttpServer -> " + format_exc())

    def get_path(self):
        url = parse.urlsplit(self.path)
        
        self.queries = {}
        d = url.query.split("&")
        if len(d[0]) != 0:
            for i in d:
                v = i.split("=")
                self.queries[v[0]] = v[1]

        path = os.path.join(self.dir, parse.unquote(url.path[1:]))

        if os.path.isdir(path):
            return os.path.join(path, "index.html")
        return path

    @property
    def download(self):
        if self.queries.get("download"):
            return True
        return False


def run(dir: str, host: str="127.0.0.1", port: int=8080, keyIntHandle: bool=True, msg: bool=True):
    handler_class = partial(HttpRequestHandler, dir=dir)
    server = ThreadingHTTPServer((host, port), handler_class)

    if msg: logging.info(f"HttpServer -> started at http://{host}:{port}")
    if keyIntHandle:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            if msg: logging.info(f"HttpServer -> stoped")
    else:
        server.serve_forever()

def get_configured_server(dir: str, host: str="127.0.0.1", port: int=8080) -> ThreadingHTTPServer:
    handler_class = partial(HttpRequestHandler, dir=dir)
    server = ThreadingHTTPServer((host, port), handler_class)
    return server

if __name__ == "__main__":
    run(os.getcwd())