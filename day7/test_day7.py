#!/usr/bin/env python

import pytest

from day7 import find_root, find_unbalanced

test_case = r"""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


def test_find_root(benchmark):
    expected = 'tknk'
    actual, _ = benchmark(find_root, test_case)
    assert expected == actual


def test_find_unbalanced(benchmark):
    expected = 60
    actual = benchmark(find_unbalanced, test_case)
    assert expected == actual
