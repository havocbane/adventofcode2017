#!/usr/bin/env python

import pytest

from day11 import shortest_path


@pytest.mark.parametrize('test_case,expected', [
    ('ne,ne,ne', 3,),
    ('ne,ne,sw,sw', 0,),
    ('ne,ne,s,s', 2,),
    ('se,sw,se,sw,sw', 3,),
])
def test_shortest_path(benchmark, test_case, expected):
    actual = benchmark(shortest_path, test_case.split(','))[0]
    assert expected == actual
