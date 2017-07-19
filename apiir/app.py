# coding=utf-8
"""APIIR Server Class
"""
from __future__ import print_function

import cherrypy

__all__ = ['App']


class App(object):
    """Endpoint App for the Apiir environment engine."""
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def default(self, *vpath, **params):
        """
        Default handler for an Apiir Endpoint.
        Handles all paths for the endpoint.
        """

        if not vpath:
            return index()
        else:
            raise cherrypy.HTTPError(404)


def index():
    """Index is a no-op"""
    return {}
