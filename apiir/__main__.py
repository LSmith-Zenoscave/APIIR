#!/usr/bin/env python
# coding=utf-8
"""The APIIR translator main script

"""
from __future__ import print_function

import getopt
import sys

import cherrypy

from apiir.server import Server


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def call(testing, opts, args):
    """main loop

    return:
        None

    """

    opts = dict(opts or [])
    for arg in args:
        pass

    Server(opts.get('port', 8080))

    engine = cherrypy.engine
    engine.signals.subscribe()
    if testing:
        cherrypy.server.unsubscribe()

    if hasattr(engine, "signal_handler"):
        engine.signal_handler.subscribe()

    if hasattr(engine, "console_control_handler"):
        engine.console_control_handler.subscribe()

    engine.start()
    if not testing:
        engine.block()
    return 0


def main(argv=None, testing=False):
    """main runner

    return:
        None

    """
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hp:", ["help", "port="])
        except getopt.error as msg:
            raise Usage(msg)

        return call(testing, opts, args)

    except Usage as err:
        print(err.msg, file=sys.stderr)
        print("For help, use --help", file=sys.stderr)
        return 127


if __name__ == '__main__':
    sys.exit(main())
