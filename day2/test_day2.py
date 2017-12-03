#!/usr/bin/env python

import pytest

from day2 import checksum, checksum_evenly_divided


def test_checksum(benchmark):
    data = r"""5 1 9 5
7 5 3
2 4 6 8
"""
    expected = 18
    actual = benchmark(checksum, data)
    assert expected == actual


def test_checksum_evenly_divided(benchmark):
    data = r"""5 9 2 8
9 4 7 3
3 8 6 5"""
    expected = 9
    actual = benchmark(checksum_evenly_divided, data)
    assert expected == actual
