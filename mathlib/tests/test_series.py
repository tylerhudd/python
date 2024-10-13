import pytest
from mathlib.series import *

def test_sum_integers() -> None:
    try:
        assert(sum_integers(1) == 1)
        assert(sum_integers(1000, 3) == 166833)
        assert(sum_integers(22, 3, 7) == 9 + 12 + 15 + 18 + 21)
        assert(sum_integers(22, 3, 6) == 6 + 9 + 12 + 15 + 18 + 21)
        assert(sum_integers(22, 3, 5) == 6 + 9 + 12 + 15 + 18 + 21)
    except Exception as e:
        pytest.fail(f"Failed to test summing integers: {e}")

def test_get_fibonnaci() -> None:
    try:
        assert(get_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8, 13])
        assert(get_fibonacci(7,2) == [1, 2, 3, 5, 8, 13])
        assert(get_fibonacci(max=100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
    except Exception as e:
        pytest.fail(f"Failed to get fibonacci sequence: {e}")
    
    test_vector = [(1.0,), (1, 1.0), (1, 1, 1.0), (1, 3), ()]
    for v in test_vector:
        with pytest.raises(ValueError) as e_info:
            get_fibonacci(*v)
        assert str(e_info)
