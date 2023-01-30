

class Headers:

    def __init__(self,requests_handler, headers: dict=None):
        self.requests_handler = requests_handler
        self.headers = headers
        
        default_headers = {
            "Content-Type": "text/html",
            # Set CORS headers
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        
        for key in default_headers:
            if key not in self.headers.keys():
                self.headers[key] = default_headers.get(key)

    def send(self, response_code: int, key: str=None) -> "Headers":
        self.requests_handler.send_response(response_code)
        for k, v in self.headers.items() if key == None else self.headers_contianer[key].items():
            self.requests_handler.send_header(k, v)
        
        return self

    def end(self) -> None:
        """`requests_handler.end_headers()`"""
        self.requests_handler.end_headers()


