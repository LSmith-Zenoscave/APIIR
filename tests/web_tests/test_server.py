from __future__ import unicode_literals

import cherrypy

from apiir.server import Server
from tests.web_tests.cptestcase import BaseCherryPyTestCase


def setUpModule():
    Server(8080)
    engine = cherrypy.engine
    engine.signals.subscribe()

    if hasattr(engine, "signal_handler"):
        engine.signal_handler.subscribe()

    if hasattr(engine, "console_control_handler"):
        engine.console_control_handler.subscribe()

    engine.start()


setup_module = setUpModule


def tearDownModule():
    cherrypy.engine.exit()


teardown_module = tearDownModule


class TestApiir(BaseCherryPyTestCase):
    def test_index(self):
        response = self.request('/')
        self.assertEqual(response.output_status, b'200 OK')
        self.assertEqual(response.body, [b'{}'])

    def test_404(self):
        response = self.request('/404')
        self.assertEqual(response.output_status, b'404 Not Found')


if __name__ == '__main__':
    import unittest
    unittest.main()
