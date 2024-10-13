import pytest
from mathlib.plotting import plot_2d_function
from mathlib.probability import *
from functools import partial
from icecream import ic

def test_normal_pdf_plot():
    try:
        # Use functools.partial to create functions with different means and sigmas
        normal_pdf_mean0_sigma1 = partial(normal_pdf, mean=0, sigma=1)
        normal_pdf_mean0_sigma1.__name__=r"$\mu=0, \sigma=1$"
        normal_pdf_mean1_sigma2 = partial(normal_pdf, mean=1, sigma=2)
        normal_pdf_mean1_sigma2.__name__=r"$\mu=1, \sigma=2$"
        normal_pdf_mean2_sigma0_5 = partial(normal_pdf, mean=2, sigma=0.5)
        normal_pdf_mean2_sigma0_5.__name__=r"$\mu=2, \sigma=0.5$"
        
        normal_pdfs = [ \
            normal_pdf_mean0_sigma1,
            normal_pdf_mean1_sigma2,
            normal_pdf_mean2_sigma0_5]
        
        normal_df_title=r"Normal Distribution $\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$"

        plot_2d_function(normal_pdfs, x_min=-5, x_max=5, num_points=1000, title=normal_df_title)

    except Exception as e:
        pytest.fail(f"Failed to plot normal distribution: {e}.")


def test_coin_toss():
    try:
        num_tosses = 10

        all_heads = ['H']*num_tosses
        heads_toss = [coin_toss(1) for _ in range(num_tosses)]
        assert(all_heads == heads_toss)

        tails_toss = [coin_toss(0) for _ in range(num_tosses)]
        all_tails = ['T']*num_tosses
        assert(tails_toss == all_tails)

    except Exception as e:
        pytest.fail(f"Failed to toss coin: {e}")

def test_die_roll():
    try:
        num_faces = 6
        num_rolls = 10
        weights = [1] + [0]*(num_faces-1)

        for f in range(num_faces):
            expected = [f+1]*num_rolls
            rolls = [die_roll(weights=weights) for _ in range(num_rolls)]
            assert(rolls == expected)
            print(weights, rolls, expected)
            weights = [0] + weights[:-1]
    except Exception as e:
        pytest.fail(f"Failed to roll die: {e}")

def test_fact() -> int:
    #TODO
    pass

def test_n_choose_k() -> int:
    #TODO
    pass

def test_pascals_triangle() -> list:
    #TODO
    pass

def test_print_pascals_triangle() -> None:
    #TODO
    pass

def test_binomial_pmf() -> None:
    #TODO
    pass

def test_plot_binomial_pmf() -> None:
    #TODO
    pass

def test_geometric_pmf() -> None:
    #TODO
    pass

def test_plot_geometric_pmf() -> None:
    #TODO
    pass

def test_poisson_pmf() -> None:
    #TODO
    pass

def test_plot_poisson_pmf() -> None:
    #TODO
    pass

