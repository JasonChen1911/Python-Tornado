# -*- coding:utf8 -*-

from tornado.web import asynchronous
from tornado.ioloop import IOLoop
from handlers.base import BaseHandler
import time

class SleepHandler(BaseHandler):
    @asynchronous
    def get(self):
        IOLoop.instance().add_timeout(time.time() + 17, callback=self.on_response)
        #time.sleep(17)
        #self.render("sleep.html")

    def on_response(self):
        self.render("sleep.html")
        self.finish()


class SeeHandler(BaseHandler):
    def get(self):
        self.render("see.html")