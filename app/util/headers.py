

class Headers:

    def __init__(self,requests_handler, headers: dict=None):
        self.requests_handler = requests_handler
        self.headers = headers

    def send(self, response_code: int, key: str=None) -> "Headers":
        self.requests_handler.send_response(response_code)
        for k, v in self.headers.items() if key == None else self.headers_contianer[key].items():
            self.requests_handler.send_header(k, v)
        
        return self

    def end(self) -> None:
        """`requests_handler.end_headers()`"""
        self.requests_handler.end_headers()


