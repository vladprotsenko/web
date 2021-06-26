def app(environ, start_response):
#    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    body = '\n'.join(environ.get('QUERY_STRING').split('&'))
    start_response("200 OK", [
        ("Content-Type", "text/plain"), 
        ("Content-Length", str(len(body)))
    ])
    return body
