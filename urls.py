#-*- coding:utf8 -*-

'''
the url structure of website
'''

import sys
from handlers.Main import MainHandler
from handlers.index import IndexHandler
from handlers.user import UserHandler

urls = [
    #(r'/', MainHandler, {'title':'百度'}),
    (r'/', IndexHandler),
    (r'/user', UserHandler),
]