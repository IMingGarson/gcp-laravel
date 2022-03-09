from pprint import pprint

class BaseMiddleware(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        pprint(environ)
        return self.app(environ, start_response)