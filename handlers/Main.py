# -*- coding:utf8 -*-

from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    def initialize(self, title):
        self.title = title
    def get(self):
        self.write("<h1>您在浏览的网站是：%s</h1>" %self.title)