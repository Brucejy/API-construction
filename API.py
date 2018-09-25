import os
import tornado.web
import tornado.ioloop
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        jj = {"a": 2, "b": 3}
        self.write(jj)

    def post(self):
        a = self.get_argument('a')
        b = self.get_argument('b')
        sum = int(a) + int(b)
        sum_json = json.dumps(sum)
        self.write(sum_json)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()