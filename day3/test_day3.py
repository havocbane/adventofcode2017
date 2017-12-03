import pytest

from day3 import spiral_memory
from day3_part2 import spiral_memory as spiral_memory2


@pytest.mark.parametrize('test_case,expected', [
    (1, 0,),
    (12, 3,),
    (23, 2,),
    (49, 6),
    (1024, 31,),
])
def test_spiral_memory(test_case, expected):
    actual = spiral_memory(test_case)
    assert expected == actual


@pytest.mark.parametrize('test_case,expected', [
    (1, 1,),
    (2, 2,),
    (4, 4,),
    (45, 54),
    (148, 304,),
    (777, 806,),
])
def test_spiral_memory2(test_case, expected):
    actual = spiral_memory2(test_case)
    assert expected == actual
