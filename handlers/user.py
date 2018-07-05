# -*- coding:utf8 -*-

from tornado.web import RequestHandler
import methods.readdb as mrd


class UserHandler(RequestHandler):
    def get(self):
        username = self.get_argument("username")
        user_info = mrd.select_table(table="users", column="*", condition="username", value=username)
        self.render("user.html", userinfo = user_info)
