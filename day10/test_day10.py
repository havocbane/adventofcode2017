#!/usr/bin/env python

import pytest

from day10 import knot_hash


def test_knot_hash():#benchmark):
    test_case = '3, 4, 1, 5'  # input lengths
    expected = 12
    #actual = benchmark(knot_hash, test_case, 5)
    actual = knot_hash(test_case, 5)
    assert expected == actual
