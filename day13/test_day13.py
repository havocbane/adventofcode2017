#!/usr/bin/env python

import pytest

from day13 import packet_riding


def test_packet_riding(benchmark):
    test_case = r"""0: 3
1: 2
4: 4
6: 4
"""
    expected = 24
    actual = benchmark(packet_riding, test_case)
    assert expected == actual
