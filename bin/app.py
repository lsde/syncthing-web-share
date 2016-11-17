#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
import os

DOMAIN = os.environ['DOMAIN']
PORT = int(os.environ['PORT'])

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.headers['Host'] == DOMAIN:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.send_response(301)
            new_path = "https://www.{0}{1}".format(self.headers['Host'],self.path)
            self.send_header('Location', new_path)
            self.end_headers()

handler = SocketServer.TCPServer(("", PORT), myHandler)
print "serving at port {0}".format(PORT)
try:
    handler.serve_forever()
except KeyboardInterrupt:
    handler.server_close()
