# Python http.server that sets Access-Control-Allow-Origin header.
# https://gist.github.com/razor-x/9542707

import os
import sys
import http.server
import socketserver

PORT = 9000

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

def server(port):
    HTTPRequestHandler.extensions_map['.wasm'] = 'application/wasm'
    httpd = socketserver.TCPServer(('', port), HTTPRequestHandler)
    return httpd

if __name__ == "__main__":
    port = PORT
    httpd = server(port)
    try:
        os.chdir('pyodide/build/')
        print("\nserving from build/ at localhost:" + str(port))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n...shutting down http server")
        httpd.shutdown()
        sys.exit()
