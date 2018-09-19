import os
import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, SELECT\n")

    def post(self):
        self.write("Hello, ADD\n")

    def put(self):
        self.write("Hello, UPDATE\n")

    def delete(self):
        self.write("Hello, DELETE\n")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()