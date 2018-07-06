#-*- coding:utf8 -*-

'''
the url structure of website
'''

import sys
from handlers.Main import MainHandler
from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.sleep import *
from handlers.Sign import *

urls = [
    #(r'/', MainHandler, {'title':'百度'}),
    (r'/', IndexHandler),
    (r'/SignIn', SignInHandler),
    (r'/SignOn', SeeHandler),
    (r'/user', UserHandler),
    (r'/sleep', SleepHandler),
    (r'/see', SeeHandler),
]