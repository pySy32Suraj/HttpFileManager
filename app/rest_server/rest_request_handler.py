import logging
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


    def do_GET(self):
        try:
            if self.path == "/favicon.ico":
                return
            self.make_response()
        except Exception:
            Headers(self, {
                "Content-Type": "text/html"
            }).send(HTTPStatus.INTERNAL_SERVER_ERROR).end()
            
            self.wfile.write(format_exc().replace("\n", "</br>").encode("utf-8"))
            logging.error("RestServer -> " + format_exc())

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
    
