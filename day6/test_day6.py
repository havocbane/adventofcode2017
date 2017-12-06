#!/usr/bin/env python

import pytest

from day6 import debugger


def test_debugger(benchmark):
    test_case = "0\t2\t7\t0\n"
    expected = 5
    actual = benchmark(debugger, test_case)
    assert expected == actual
