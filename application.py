# -*- coding:utf8 -*-

from urls import urls
from tornado.web import Application
import os
import base64, uuid

cookie_secret_value = base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes)
#print(cookie_secret_value)
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), 'templates'),#模板路径
    static_path = os.path.join(os.path.dirname(__file__), 'statics'),#静态文件路径
    cookie_secret = cookie_secret_value, #cookie
    xsrf_cookies = True, #开启 XSRF 保护， XSRF即跨站请求伪造
    login_url = '/',
)

application = Application(
    handlers=urls,
    **settings,
    debug=True
)