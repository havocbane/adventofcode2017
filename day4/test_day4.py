#!/usr/bin/env python

import pytest

from day4 import valid_passphrases, valid_passphrases_anagrams


def test_passphrases(benchmark):
    data = r"""aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa"""
    expected = 2
    actual = benchmark(valid_passphrases, data)
    assert expected == actual


def test_passphrases_with_anagrams(benchmark):
    data = r"""abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio"""
    expected = 3
    actual = benchmark(valid_passphrases_anagrams, data)
    assert expected == actual
