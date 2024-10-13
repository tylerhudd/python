import pytest
from mathlib.util import *

def test_get_prime_factors() -> None:
    test_vector = [
        (1, []),
        (2, [2]),
        (3, [3]),
        (6, [2,3]),
        (13195, [5, 7, 13, 29]),
        (600851475143, [71, 839, 1471, 6857]) ]
    
    for v in test_vector:
        try:
            assert(get_prime_factors(v[0]) == v[1])
        except Exception as e:
            pytest.fail(f"Failed to find prime factors: {e}")