#-*- coding:utf8 -*-

'''
the url structure of website
'''

import sys
from handlers.index import IndexHandler
from handlers.user import *
from handlers.sleep import *
from handlers.Sign import *
from handlers.SignOn import *

urls = [
    (r'/', IndexHandler),
    (r'/SignIn', SignInHandler),
    (r'/SignOn', SignOnHandler),
    (r'/user', UserHandler),
    (r'/sleep', SleepHandler),
    (r'/see', SeeHandler),
    (r'/success', SuccessHandler),
]