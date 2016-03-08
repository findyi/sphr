# coding:utf8

"""
Copyright 2016 Smallpay Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import tornado.web
import tornado.ioloop
import tornado.httpserver
import venusian
import os
import sphr.restapi


class HttpApplication(tornado.web.Application):

    HANDLERS = []

    def route(self, pattern, kwargs=None, name=None):
        def decorator(cls):
            self.add_handler(pattern, cls, kwargs, name)
            return cls
        return decorator

    def add_handler(self, pattern, cls, kwargs=None, name=None):
        self.HANDLERS.append((pattern, cls, kwargs, name))

    def finish_route(self):
        self.add_handlers(".*$", self.HANDLERS)

app = HttpApplication()


def start_http_server(port=8888):
    ioloop = tornado.ioloop.IOLoop.instance()

    scanner = venusian.Scanner()
    scanner.scan(sphr.restapi)

    app.add_handler(r"/ngapp/(.*)$", tornado.web.StaticFileHandler, {'path': os.path.join(os.getcwd(), '../ngapp')})
    app.finish_route()

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port)
    ioloop.start()


if __name__ == '__main__':
    start_http_server()