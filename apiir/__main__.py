#!/usr/bin/env python
# coding=utf-8
"""The APIIR translator main script

"""
from __future__ import print_function

import getopt
import sys


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def call(opts, args):
    """main loop

    return:
        None

    """

    opts = dict(opts or [])
    for arg in args:
        pass

    return 0


def main(argv=None):
    """main runner

    return:
        None

    """
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error as msg:
            raise Usage(msg)

        return call(opts, args)

    except Usage as err:
        print(err.msg, file=sys.stderr)
        print("For help, use --help", file=sys.stderr)
        return 127


if __name__ == '__main__':
    sys.exit(main())
