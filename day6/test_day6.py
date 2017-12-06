#!/usr/bin/env python

import pytest

from day6 import debugger


def test_debugger(benchmark):
    test_case = "0\t2\t7\t0\n"
    expected_cycles = 5
    expected_loops_since_cycle = 4
    actual_cycles, actual_loops_since_cycle = benchmark(debugger, test_case)
    assert expected_cycles == actual_cycles
    assert expected_loops_since_cycle == actual_loops_since_cycle
