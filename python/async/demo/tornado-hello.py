import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    print("Serve http://127.0.0.1:8888/")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
