def app(environ, start_response):
    body = [bytes(i + '\n') for i in environ['QUERY_STRING'].split('&')]
#    start_response("200 OK", [
#        ("Content-Type", "text/plain"),
#        ("Content-Length", str(len(body)))
#    ])
    return body
