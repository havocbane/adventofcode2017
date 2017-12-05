#!/usr/bin/env python

import pytest

from day5 import exit_maze


def test_exit_maze(benchmark):
    instructions = "0\n3\n0\n1\n-3"
    expected = 5
    actual = benchmark(exit_maze, instructions)
    assert expected == actual
