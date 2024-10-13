import pytest
import numpy as np
from mathlib.probability import normal_pdf
from mathlib.calc import *

def test_normal_pdf_plot():
    try:
        area1 = integrate(lambda x: np.exp(-x**2), -10, 10, 0.1)
        differr1 = abs((np.sqrt(np.pi)-area1)/np.sqrt(np.pi))
        assert(differr1 < 0.0000001)

        area2 = integrate(normal_pdf, -10, 10, 0.1)
        differ2 = abs(1-area2)
        assert(differ2 < 0.0000001)

    except Exception as e:
        pytest.fail(f"Failed integration test: {e}.")