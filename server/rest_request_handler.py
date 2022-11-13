from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from utilits.path_argument_parser import PathArgumentParser

class RestRequestHandler(BaseHTTPRequestHandler):
    # Map the functions by path
    get_PathMap: dict = {} # for 'GET' method requests maped here by their path.

    # In the maped functions need to send status code before anything you to send.

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
            self.make_response()
        except Exception as e:
            self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(e.__str__().encode("utf-8"))
            self.log_error(e.__str__())

    def make_response(self):
        parser = PathArgumentParser()
        p_args = parser.parse(self.path)
        item = RestRequestHandler.get_PathMap.get(p_args["Path"])
       
        if item:
            if item["ParametersTypes"]:
                
                if p_args["Arguments"]:
                    args = parser.type_cast(item["ParametersTypes"], p_args["Arguments"])
                    print(args, p_args)
                    r = item["func"](self, **args)
                else:
                    r = item["func"](self)
                
            else:
                r = item["func"](self)
            
            self.end_headers()
            
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