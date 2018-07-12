#-*- coding:utf8 -*-

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
            self.write("1")
        else:
            if password1 == password2:
                user_insert = mrd.insert_row(table="users",user=username, pwd=password1, email=email)
                self.set_current_user(username)
                self.write(username)
            else:
                self.write("-1")
    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', json_encode(user))
        else:
            self.clear_cookie("user")