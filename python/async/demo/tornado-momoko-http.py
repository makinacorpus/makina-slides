import json
import tornado.web
import tornado.httpclient
import tornado
import momoko


class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        def handle_db(cursor, error):
            db_value = cursor.fetchone()[0]

            def handle_http(response):
                json_data = json.loads(response.body.decode())
                result = db_value - json_data['value']
                self.write("Result: %s" % result)
                self.finish()

            http_client = tornado.httpclient.AsyncHTTPClient()
            http_client.fetch('http://127.0.0.1:8000/', handle_http)
        self.application.db.execute(
            'SELECT 42, pg_sleep(0.300)', callback=handle_db)


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    print("Serve http://127.0.0.1:8888/")
    application.db = momoko.Pool(dsn='dbname=al user=al', size=10)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
