#!/usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import http


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/test", MainHandler),
    ])


if __name__ == "__main__":
    print("1111")
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
