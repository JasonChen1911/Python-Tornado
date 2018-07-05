# -*- coding:utf8 -*-

from tornado.web import authenticated
import methods.readdb as mrd
from tornado.escape import json_decode
from handlers.base import BaseHandler


class UserHandler(BaseHandler):
    @authenticated
    def get(self):
        #username = self.get_argument("username")
        username = json_decode(self.current_user)
        user_info = mrd.select_table(table="users", column="*", condition="username", value=username)
        self.render("user.html", userinfo = user_info)
