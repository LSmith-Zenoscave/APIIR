# coding=utf-8
"""
apiir.__main__ Tests
"""
from __future__ import print_function

from nose.tools import assert_false

from apiir.__main__ import main


class TestAPIIR(object):
    """Tests the main call method and argument/options parser.

    """
    def test_it_runs(self):
        raised = False
        try:
            main()
        except:
            raised = True
        assert_false(raised, "Should Always run")
