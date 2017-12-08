#!/usr/bin/env python

import pytest

from day8 import compute_largest_register


def test_registers(benchmark):
    test_case = r"""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
    expected_largest_at_end = 1
    expected_largest_seen = 10
    actual_largest_at_end, actual_largest_seen = benchmark(compute_largest_register, test_case)
    assert expected_largest_at_end == actual_largest_at_end
    assert expected_largest_seen == actual_largest_seen
