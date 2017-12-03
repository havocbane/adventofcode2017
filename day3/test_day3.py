import pytest

from day3 import spiral_memory


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
