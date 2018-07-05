# -*- coding:utf8 -*-

from tornado.web import RequestHandler
import methods.readdb as mrd
from handlers.base import BaseHandler
from tornado.escape import json_encode

class IndexHandler(BaseHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', "*")

    def get(self):
        usernames = mrd.select_columns(table="users", column="username")
        one_user = usernames[0][0]
        self.render("index.html", user = one_user) #render() 函数的功能在于向请求者反馈网页模板，并且向模板中传递数值

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][1]
            if db_pwd == password:
                self.set_current_user(username)
                self.write(username)
            else:

                self.write("-1")
        else:
            self.write("-1")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', json_encode(user))
        else:
            self.clear_cookie("user")

class ErrorHandler(BaseHandler):
    def get(self):
        self.render("error.html")
