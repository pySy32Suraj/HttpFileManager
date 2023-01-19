import os
import shutil
import posixpath
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from util.path_argument_parser import PathArgumentParser
from util.exc_formater import format_exc
from util.headers import Headers

__version__ = "v1.0"


class RestRequestHandler(BaseHTTPRequestHandler):
    # Map the functions by path
    get_PathMap: dict = {} # for 'GET' method requests maped here by their path.

    # In the maped functions need to send status code before anything you to send.
    server_version = "RestRequestHandler/" + __version__
    
    """
    default parameters will parse as str
    type :- str, int, float, bool
    specify: type: para-name
    Example:

        @RestRequestHandler.get("/?name&int: age")
        def home(cls, name, age):
            cls.send_response(200)
            cls.send_header("Content-type", "application/json")
            ...
    """

    extensions_map = {
        '.gz': 'application/gzip',
        '.Z': 'application/octet-stream',
        '.bz2': 'application/x-bzip2',
        '.xz': 'application/x-xz',
    }

    def do_HEAD(self):
        print("head is invoked")

    def do_GET(self):
        # self.log_message(f"GET : {self.path}")
        
        try:
            if self.path == "/favicon.ico":
                self.get_favicon()
                return

            self.make_response()
        except Exception as e:
            self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(format_exc().replace("\n", "</br>").encode("utf-8"))
            self.log_error(format_exc())

    def make_response(self):
        parser = PathArgumentParser()
        p_args = parser.parse(self.path)
        item = RestRequestHandler.get_PathMap.get(p_args["Path"])
        
        if item == None:
            raise NotImplementedError("This end point might be not implemented yet.", p_args["Path"])
        
        if item:
            if item["ParametersTypes"]:
                
                if p_args["Arguments"]:
                    args = parser.type_cast(item["ParametersTypes"], p_args["Arguments"])
                    r = item["func"](self, **args)
                else:
                    r = item["func"](self)
                
            else:
                r = item["func"](self)
 
            if r != None:
                self.wfile.write(bytes(r, "utf-8"))

    def get_favicon(self):
        if not hasattr(self, "favicon_path"):
            self.favicon_path = os.path.join(os.getcwd(), "favicon.ico")
        if not os.path.exists(self.favicon_path):
            raise FileNotFoundError(self.favicon_path)
        
        self.send_file(self.favicon_path, self.wfile)
        return "Hello"

    def send_file(self, fpath: str, for_download: bool=False):
        print("Sending the file : ", fpath)
        h = Headers(self, {
            "Content-Type": self.guess_type(fpath),
            "Content-Length": os.path.getsize(fpath)
        })
        h.send(HTTPStatus.OK)
        h.end()
        print(self.headers)

        try:
            f = open(fpath, "rb")
            self.wfile.write(f.read())
        except OSError:
            pass
        finally:
            f.close()
        # with open(fpath, "rb") as f:
        #     shutil.copyfileobj(f, self.wfile)

    def guess_type(self, path):
        """Guess the type of a file.

        Argument is a PATH (a filename).

        Return value is a string of the form type/subtype,
        usable for a MIME Content-type header.

        The default implementation looks the file's extension
        up in the table self.extensions_map, using application/octet-stream
        as a default; however it would be permissible (if
        slow) to look inside the data to make a better guess.

        """
        base, ext = posixpath.splitext(path)
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        ext = ext.lower()
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        guess, _ = mimetypes.guess_type(path)
        if guess:
            return guess
        return 'application/octet-stream'

    @staticmethod
    def get(pathStr):
        parser = PathArgumentParser()
        path, para = parser.split_path_para(pathStr)

        def wraper(func):
            RestRequestHandler.get_PathMap[path] = {
                "func": func,
                "ParametersTypes": parser.para_types_class(para) if para != None else None
            }
        
        return wraper
    
