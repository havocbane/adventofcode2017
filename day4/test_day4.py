#!/usr/bin/env python

import pytest

from day4 import valid_passphrases


def test_passphrases(benchmark):
    data = r"""aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa"""
    expected = 2
    actual = benchmark(valid_passphrases, data)
    assert expected == actual
