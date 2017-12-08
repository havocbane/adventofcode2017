#!/usr/bin/env python

import pytest

from day8 import compute_largest_register


def test_registers(benchmark):
    test_case = r"""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
    expected = 1
    actual = benchmark(compute_largest_register, test_case)
    assert expected == actual
