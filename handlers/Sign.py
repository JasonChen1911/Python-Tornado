# -*- coding:utf8 -*-

from tornado.web import RequestHandler
from tornado.escape import json_encode
import methods.readdb as mrd

class SignOnHandler(RequestHandler):
    def get(self):
        self.render("SignOn.html")

    def post(self):
        username = self.get_argument("username")
        password1 = self.get_argument("password1")
        password2 = self.get_argument("password2")
        email = self.get_argument("email")
        user_info = mrd.select_table(table="users", column="*", condition="username", value=username)
        if user_info:
            self.write("-1")
        else:
            if password1 == password2:
                self.write("success")
            else:
                self.write("-1")

class SignInHandler(RequestHandler):
    def get(self):
        self.render("SignIn.html")

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