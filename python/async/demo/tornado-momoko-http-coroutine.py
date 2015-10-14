import json
import tornado.web
import tornado.httpclient
import tornado
import momoko


class MainHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        cursor = yield self.application.db.execute('SELECT 42, pg_sleep(0.300)')
        db_value = cursor.fetchone()[0]
        http_client = tornado.httpclient.AsyncHTTPClient()
        response = yield http_client.fetch('http://127.0.0.1:8000/')
        json_data = json.loads(response.body.decode())
        result = db_value - json_data['value']
        self.write("Result: %s" % result)
        self.finish()


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    print("Serve http://127.0.0.1:8888/")
    ioloop = tornado.ioloop.IOLoop.instance()
    application.db = momoko.Pool(dsn='dbname=al user=al password=al',
                                 size=10, ioloop=ioloop)
    future = application.db.connect()
    ioloop.add_future(future, lambda f: ioloop.stop())
    ioloop.start()
    future.result()  # raises exception on connection error
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
