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
    actual, _ = benchmark(stream_score, test_case)
    assert expected == actual


@pytest.mark.parametrize('test_case,expected', [
    ('<>', 0,),
    ('<random characters>', 17,),
    ('<<<<>', 3,),
    ('<{!>}>', 2,),
    ('<!!>', 0,),
    ('<!!!>>', 0,),
    ('<{o"i!a,<{i<a>', 10,),
])
def test_count_non_canceled_garbage(benchmark, test_case, expected):
    _, actual = benchmark(stream_score, test_case)
    assert expected == actual
