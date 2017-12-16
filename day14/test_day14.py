#!/usr/bin/env python

import pytest

from day14 import count_squares, count_regions


def test_squares(benchmark):
    test_case = 'flqrgnkx'
    expected = 8108
    actual = benchmark(count_squares, test_case)
    assert expected == actual


def test_regions(benchmark):
    test_case = 'flqrgnkx'
    expected = 1242
    actual = benchmark(count_regions, test_case)
    assert expected == actual
