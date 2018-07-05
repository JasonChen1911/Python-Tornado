#-*- coding:utf8 -*-
#import sys
#sys.path.append('~/.pyenv/versions/3.7.0/lib/python3.7/site-packages')

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

#定义变量
tornado.options.define('port', default=8000,type=int,help="this is the port >for application")

class MainHandler(tornado.web.RequestHandler):#RequestHandler:封装对请求处理的所有信息和处理方法
    def set_default_headers(self):
        print("-----> 响应头set_default_headers()执行")
        self.set_header("Content-type", "application/json; charset=utf-8")
        self.set_header("js", "zj")
    def get(self):
        #user = self.get_argument("user")
        #print("get方式获取参数：" + str(user))
        self.write("hello jianshu.com")
        self.set_cookie("loginuser", "admin")
        print(self.get_cookie("loginuser"))
        print(self.cookies)
    def post(self):
        user = self.get_argument('user')
        print("post方式参数" + user)

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello jason")

        self.set_status(500, reason="你mmp")
        self.send_error(404, msg = "页面丢失", info = "服务器丢失")

    def write_error(self, status_code, **kwargs):
        self.write("<h1>出错啦， 工程师正在该来的途中...</h1>")
        self.write("<p>错误信息：%s</p>" %kwargs['msg'])
        self.write("<p>错误描述：%s</p>" %kwargs['info'])



def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'^/error$', ErrorHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()