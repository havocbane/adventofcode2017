#!/usr/bin/env python

import pytest

from day1 import inverse_captcha, inverse_captcha_halfway


@pytest.mark.parametrize("test_case,expected", [
    ('1122', 3,),
    ('1111', 4,),
    ('1234', 0,),
    ('91212129', 9,),
])
def test_day1(benchmark, test_case, expected):
    # benchmark.group = 'Case: {0} == {1} - perf'.format(test_case, expected)
    actual = benchmark(inverse_captcha, test_case)
    assert expected == actual


@pytest.mark.parametrize("test_case,expected", [
    ('1212', 6,),
    ('1221', 0,),
    ('123425', 4,),
    ('123123', 12,),
    ('12131415', 4,),
])
def test_day1_part2(benchmark, test_case, expected):
    # benchmark.group = 'Halfway Case: {0} == {1} - perf'.format(test_case, expected)
    actual = benchmark(inverse_captcha_halfway, test_case)
    assert expected == actual
