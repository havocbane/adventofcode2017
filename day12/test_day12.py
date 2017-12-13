#!/usr/bin/env python

import pytest

from day12 import find_zero_group_size, find_number_of_groups


test_case = r"""0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""


def test_find_zero_group_size(benchmark):
    expected = 6
    actual = benchmark(find_zero_group_size, test_case)
    assert expected == actual


def test_find_number_of_groups(benchmark):
    expected = 2
    actual = benchmark(find_number_of_groups, test_case)
    assert expected == actual
