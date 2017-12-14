#!/usr/bin/env python

import pytest

from day13 import packet_riding, find_when_not_captured


test_case = r"""0: 3
1: 2
4: 4
6: 4
"""


def test_packet_riding(benchmark):
    expected = 24
    actual = benchmark(packet_riding, test_case)
    assert expected == actual


def test_find_when_not_captured(benchmark):
    expected = 10
    actual = benchmark(find_when_not_captured, test_case)
    assert expected == actual
