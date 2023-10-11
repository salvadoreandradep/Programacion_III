from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse

import json


port = 3000

class miServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "login.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
        if self.path=="/productos.html":
            self.path = "productos.html"
            return SimpleHTTPRequestHandler.do_GET(self)
       
        if self.path=="/principal.html":
            self.path = "principal.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        
       
print("Ejecuntando server en puerto ", port)
server = HTTPServer(("localhost", port), miServer)
server.serve_forever()