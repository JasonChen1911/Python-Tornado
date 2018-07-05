# -*-coding:utf8 -*-
'''
server
'''
from tornado.httpserver import HTTPServer
from tornado.options import options, define
from tornado.ioloop import IOLoop
from application import application


define("port", default=8000, help="run on the given port", type=int)

def main():
    options.parse_command_line()
    http_server = HTTPServer(application)
    http_server.listen(options.port)

    print("Development server is running at http://127.0.0.1:%s" % options.port)
    print("Quit the server with Control-C")

    IOLoop.instance().start()

if __name__ == '__main__':
    main()