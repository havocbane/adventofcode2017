#!/usr/bin/env python

import pytest

from day9 import stream_score


@pytest.mark.parametrize('test_case,expected', [
    ('{}', 1,),
    ('{{{}}}', 6,),
    ('{{},{}}', 5,),
    ('{{{},{},{{}}}}', 16,),
    ('{<a>,<a>,<a>,<a>}', 1,),
    ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9,),
    ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9,),
    ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3,),
])
def test_stream_score(benchmark, test_case, expected):
    actual = benchmark(stream_score, test_case)
    assert expected == actual
