#!/usr/bin/env python

import pytest

from day14 import count_used_squares


def test_knot_hash(benchmark):
    test_case = 'flqrgnkx'
    expected = 8108
    actual = benchmark(count_used_squares, test_case)
    assert expected == actual
