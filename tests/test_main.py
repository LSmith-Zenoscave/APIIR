# coding=utf-8
"""
apiir.__main__ Tests
"""
from __future__ import print_function

from random import randrange

from nose.tools import assert_false

from apiir.__main__ import main


def fuzz():
    return ["".join([chr(randrange(256))
                     for _ in range(randrange(16))])
            for _ in range(randrange(16))]


class TestAPIIR(object):
    """Tests the main call method and argument/options parser.

    """
    def test_it_runs(self):
        raised = False
        try:
            main(testing=True)
            main([], testing=True)
            main(['-h'], testing=True)
            main(['-p', '8080'], testing=True)
        except:
            raised = True
        assert_false(raised, "Should Always run")

    def test_main_inputs_fuzz(self):
        for _ in range(1000):
            raised = False
            inputs = fuzz()
            try:
                main(inputs, testing=True)
            except:
                raised = True
            assert_false(raised,
                         "Input should not raise errors: " + " ".join(inputs))
