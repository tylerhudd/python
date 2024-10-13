import pytest
import numpy as np
from mathlib.plotting import *
from icecream import ic

def test_style_availability(capfd):
    # Print the available styles
    print(plt.style.available)

    # Capture the output of the print statement
    captured = capfd.readouterr()

    # Check that the output contains the desired style
    assert plot_theme in captured.out
    ic(plt.style.available)

def test_plot():
    try:
        plot_2d_function(lambda x: x**2)
    except Exception as e:
        pytest.fail(f"plot_2d_function raised an exception: {e}")

def test_plot_sin():
    try:
        plot_2d_function(lambda x: np.sin(x), x_min=-2*np.pi, x_max=2*np.pi)
    except Exception as e:
        pytest.fail(f"plot_2d_function raised an exception: {e}")

def test_plot_two_on_one():
    try:
        plot_2d_function([lambda x: np.sin(x), lambda y: np.cos(y)], x_min=-2*np.pi, x_max=2*np.pi)
    except Exception as e:
        pytest.fail(f"plot_2d_function raised an exception: {e}")

def test_3dPlot():
    try:
        # Plot e^{-(x^2 + y^2)}
        plot_3d_function(lambda x, y: np.exp(-(x**2 + y**2)), x_min=-2, x_max=2, y_min=-2, y_max=2)
    except Exception as e:
        pytest.fail(f"plot_3d_function raised an exception: {e}")
    