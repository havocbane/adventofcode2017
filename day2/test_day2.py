#!/usr/bin/env python

from day2 import checksum


def test_checksum():
    data = r"""5 1 9 5
7 5 3
2 4 6 8
"""
    expected = 18
    actual = checksum(data)
    assert expected == actual
