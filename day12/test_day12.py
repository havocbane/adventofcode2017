#!/usr/bin/env python

import pytest

from day12 import find_zero_group_size


def test_find_zero_group_size(benchmark):
    test_case = r"""0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""
    expected = 6
    actual = benchmark(find_zero_group_size, test_case)
    assert expected == actual
