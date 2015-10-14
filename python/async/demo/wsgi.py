import time


def app(environ, start_response):
    time.sleep(0.300)
    data = b'{"value": 19}'
    start_response("200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
