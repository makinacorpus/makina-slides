import tornado.ioloop
import tornado.web
import psycopg2


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cur = self.application.db.cursor()
        cur.execute("SELECT 42, pg_sleep(0.300);")
        result = cur.fetchone()
        self.write("Result: %s" % result[0])


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    print("Serve http://127.0.0.1:8888/")
    application.db = psycopg2.connect("dbname=al user=al")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
