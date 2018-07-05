# -*- coding:utf8 -*-
#用于规定字符编码，中文编码

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from tornado.httpserver import HTTPServer
from tornado.options import options, define
#定义变量
define('port', default=8000,type=int,help="this is the port >for application")

class MainHandler(RequestHandler):#RequestHandler:封装对请求处理的所有信息和处理方法
    def get(self):
        self.write("<a href='"+self.reverse_url("login")+"'>用户登录</a>")

class ArticleHandler(RequestHandler):
    def initialize(self, title):
        print('-->initialize()')
        self.title = title
    def get(self):
        self.write('你正在查看文章：%s' %self.title)

class RegistHandler(RequestHandler):
    def initialize(self, title):
        self.title = title
    def get(self, *args, **kwargs):
        self.write("注册业务处理：" + str(self.title))
class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("用户登录页面展示")
    def post(self, *args, **kwargs):
        self.post("用户登录功能处理")

if __name__ == '__main__':
    options.parse_command_line()  # 命令行参数转换
    app = Application([
        (r'/', MainHandler),
        (r'/article', ArticleHandler,{'title':'你希望自己成为什么样的人，最终就会成为那样的人。'}),
        (r'/regist', RegistHandler, {'title':'会员注册'}),
        url(r'/login', LoginHandler, name="login"),
    ], debug=True)
    #Application 路由器设置 url(r'', handler, {k,v}, name='')
    http_server = HTTPServer(app)

    http_server.bind(options.port)
    http_server.start(1)
    IOLoop.current().start()#current() 返回当前线程的IOLoop实力对象，start() 启动IOLoop实例对象的IO循环，开启监听
