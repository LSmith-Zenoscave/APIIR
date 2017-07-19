# coding=utf-8
"""APIIR Server Class
"""
import cherrypy

from apiir.app import App as Apiir


class Server(object):
    def __init__(self, port):
        # Update the global settings for the HTTP server and engine
        cherrypy.config.update({'server.socket_host': "0.0.0.0",
                                'server.socket_port': int(port),
                                'server.thread_pool': 10,
                                'engine.autoreload_on': False})
        cherrypy.tree.mount(Apiir(), '/',
                            {'/': {
                                'tools.encode.on': False,
                                'tools.gzip.on': True,
                                'tools.sessions.on': True
                            }})
