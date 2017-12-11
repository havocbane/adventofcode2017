#!/usr/bin/env python

import pytest

from day10 import knot_hash, hash


def test_knot_hash(benchmark):
    test_case = [int(el.strip()) for el in '3, 4, 1, 5'.split(',')]  # input lengths
    expected = 12
    actual = benchmark(knot_hash, test_case, list_size=5)[0]
    assert expected == actual


@pytest.mark.parametrize('test_case,expected', [
    ('', 'a2582a3a0e66e6e86e3812dcb672a272',),
    ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd',),
    ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d',),
    ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e',),
])
def test_hash(benchmark, test_case, expected):
    actual = benchmark(hash, test_case)
    assert expected == actual
