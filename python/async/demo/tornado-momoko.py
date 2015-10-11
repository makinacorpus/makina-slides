import tornado.ioloop
import tornado.web
import momoko


class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        self.application.db.execute(
            'SELECT 42, pg_sleep(0.300)', callback=self._done)

    def _done(self, cursor, error):
        result = cursor.fetchone()
        self.write("Result: %s" % result[0])
        self.finish()


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    print("Serve http://127.0.0.1:8888/")
    application.db = momoko.Pool(dsn='dbname=al user=al', size=10)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
