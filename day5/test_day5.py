#!/usr/bin/env python

import pytest

from day5 import exit_maze, exit_maze_with_check


@pytest.mark.parametrize('fn,expected', [
    (exit_maze, 5,),
    (exit_maze_with_check, 10),
])
def test_exit_maze(benchmark, fn, expected):
    instructions = "0\n3\n0\n1\n-3"
    actual = benchmark(fn, instructions)
    assert expected == actual
