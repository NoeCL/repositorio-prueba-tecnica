import json
import urllib.parse
from http import HTTPStatus
from Connector import get_properties, get_propertie_by_city
from http.server import *

class Httpserver1(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(HTTPStatus.OK)
        self.send_headers("Content-Type", "application/json")
        self.end_headers()
    
    def do_GET(self):

        self.send_response(200)
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)
        print(params)
        filter_value = params.get('city',[None])[0]
        content = {}
        if filter_value: 
            print('si hay valor')
            content = json.dumps(get_propertie_by_city(filter_value))
        else:
            print('no hay valor')
            content = json.dumps(get_properties())

        self.send_header('content-type', 'application/json')
        self.end_headers()
        ##content = json.dumps({"hola":"mundo"})
       
        self.wfile.write(bytes(content,"UTF-8"))

port = HTTPServer(('', 8080), Httpserver1)

port.serve_forever()

