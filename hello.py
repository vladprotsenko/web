def app:
    "\n".join(environ.get('QUERY_STRING').split("&"))
