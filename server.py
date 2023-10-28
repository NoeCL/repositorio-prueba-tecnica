import json
from http import HTTPStatus
from Connector import get_properties
from http.server import *

class Httpserver1(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(HTTPStatus.OK)
        self.send_headers("Content-Type", "application/json")
        self.end_headers()
    
    def do_GET(self):

        self.send_response(200)

        self.send_header('content-type', 'application/json')
        self.end_headers()
        ##content = json.dumps({"hola":"mundo"})
        content = json.dumps(get_properties())
        self.wfile.write(bytes(content,"UTF-8"))

port = HTTPServer(('', 8080), Httpserver1)

port.serve_forever()

