#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler
import datetime
import random

places = [
    'Tenmimi',
    'Umai',
    'Cibo Thai',
    'Kebab Daddy',
    'Blue Fish',
    'Joselitos',
    'Seasoning Alley',
    'Etc Gourmet',
    'The fake french place',
    'Pho22',
    'Elbow Room'
]

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        today = datetime.datetime.today().strftime("%Y%m%d%H")
        random.seed(today)
        randint = random.randint(0,len(places) - 1)
        random_place = places[randint]
        message = '\n'.join([
            '%s' % random_place,
            ''
        ]).encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()
