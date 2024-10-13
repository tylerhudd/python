# mathlib/probability.py
import numpy as np
from functools import partial
from random import uniform, choices
from math import pow
from mathlib.plotting import plot_bar_chart, plot_2d_function

def normalize(data:list|tuple) -> list:
    """
    Normalize a list of data to 1.

    Parameters:
    - data: the list or tuple to normalize.
    """
    total = sum(data)
    return [d/total for d in data]

def die_roll(num_faces:int=6, weights:list|tuple=None, plot_weights:bool=False):
    """
    Simulate the roll of a die. If no weights are specified, the die roll
    is modeled as fair.

    Parameters
    - num_faces: the number of faces on the die.
    - weights: a list of biases or weights associated with each face of the die.
    """

    # generate a list of die faces
    faces = list(range(1, num_faces+1))

    # make sure there is a list of weights normalized to 1
    if not weights:
        weights = normalize([1]*num_faces)
    elif not sum(weights) == 1:
        weights = normalize(weights)
    elif len(weights) != num_faces:
        raise ValueError("The length of the weights list must match the number of faces.")
    
    return choices(faces, weights)[0]

def normal_pdf(x:float, mean:float=0, sigma:float=1) -> float:
    """
    The Normal/Gaussian/Bell curve probability distribution function.

    Parameters:
    - x: the dependent variable.
    - mean: mu, the mean of the probability distribution.
    - sigma: the standard deviation from the mean.
    """
    return 1/np.sqrt(2 * np.pi * sigma**2) * np.exp(-(x-mean)**2/(2*sigma**2))

def coin_toss(bias=0.5) -> chr:
    """
    Coin toss simulation.

    Parameters:
    - bias: the bias from 0 to 1 of flipping a Heads
    """

    # generate a random coin toss
    if uniform(0,1) < bias:
        return 'H'
    else:
        return 'T'
    
def fact(n: int) -> int:
    """
    Performs a factorial operation, n!
    """
    if n < 0:
        raise ValueError("n cannot be negative in n! operation.")
    
    running_prod = 1
    for i in range(1, n + 1):
        running_prod *= i
    
    return running_prod

def n_choose_k(n: int, k: int) -> int:
    """
    Performs n choose k operation or produces binomial coefficient.

    Parameters
    - n: total number of elements to choose from in a set
    - k: number of elements chosen - number of elements in a subset
    """
    return fact(n) // (fact(k) * fact(n - k))

def pascals_triangle(n: int) -> list:
    """
    Generate Pascal's triangle to a desired number of rows.

    Parameters
    - n: number of rows to generate.
    """
    triangle = []
    for i in range(0, n):
        triangle.append([n_choose_k(i, k) for k in range(0, i + 1)])
    
    return triangle

def print_pascals_triangle(n: int) -> None:
    """
    Print out Pascal's triangle to a desired number of rows.

    Parameters
    - n: number of rows in the triangle to print.
    """
    # generate triangle
    triangle = pascals_triangle(n)

    # Find the width of the longest row when converted to string
    longest_row = triangle[-1]
    max_width = len(' '.join(map(str, longest_row)))

    # Print each row, centered to match the width of the longest row
    for row in triangle:
        row_str = ' '.join(map(str, row))
        print(row_str.center(max_width))

def binomial_pmf(n:int, k:int, p:float) -> float:
    """
    The probability that an event with probability p
    occurs k times over n trials.

    Parameters
    - n: total number of trials
    - k: number of expected occurrences
    - p: probability of the event
    """
    if not n > 0:
        assert ValueError("n must be a positive integer")
    if not k > 0 and not k <= n:
        assert ValueError("k must be positive and less than or equal to n")
    if not p < 1 and p > 0:
        assert ValueError("p must be in the range (0,1).")

    return n_choose_k(n, k) * pow(p,k) * pow(1-p,n-k)

def plot_binomial_pmf(n: int, p: float) -> None:
    """
    Plots the binomial PMF for all k from 0 to n.

    Parameters
    - n: total number of trials
    - p: probability of success
    """
    
    # Generate all k values from 0 to n
    k_values = list(range(0, n + 1))
    
    # Calculate the PMF for each k
    pmf_values = [binomial_pmf(n, k, p) for k in k_values]

    plot_bar_chart(k_values, pmf_values, "Binomial pmf", "Event", "Probability")

def geometric_pmf(k:int, p:float) -> float:
    """
    The probability that an event with probability p will occur
    on the kth trial.

    Parameters
    - k: number of trials
    - p: probability of the event
    """
    if not p < 1 and not p > 0:
        assert ValueError("p must be in the range (0,1).")

    return pow(1-p,k-1) * p

def plot_geometric_pmf(k_max: int, p:float) -> None:
    """
    Plots the geometric PMF for all k from 0 to k_max.

    Parameters
    - k_max: maximum number of k to plot
    - p: probability of the event
    """
    
    # Generate all k values from 0 to n
    k_values = list(range(1, k_max + 1))
    
    # Calculate the PMF for each k
    pmf_values = [geometric_pmf(k, p) for k in k_values]

    plot_bar_chart(k_values, pmf_values, "Geometric pmf", "Event", "Probability")

def poisson_pmf(k:int, l:float) -> float:
    """
    The Poisson pmf related to queuing theory.

    Parameters
    - k: number of trials
    - l: lambda or rate parameter in (0, infinity)
    """
    return pow(l,k)*np.exp(-l) / fact(k)

def plot_poisson_pmf(k_max: int, l:float) -> None:
    """
    Plots the Poisson PMF for all k from 0 to k_max.

    Parameters
    - k_max: maximum number of k to plot
    - l: lambda or rate parameter in (0,infinity)
    """
    
    # Generate all k values from 0 to n
    k_values = list(range(1, k_max + 1))
    
    # Calculate the PMF for each k
    pmf_values = [poisson_pmf(k, l) for k in k_values]

    plot_bar_chart(k_values, pmf_values, "Poisson pmf", "Event", "Probability")

def uniform_pdf(r:float|list, a:float, b:float) -> float:
    """
    Returns the value of f(r) in a uniform p.d.f. If a <= r <= b, the value
    1/(b-a) (a constant) is returned. Otherwise 0 is returned.

    Parameters
    - r: dependent varaible
    - a: lower limit of the pdf
    - b: upper limit of the pdf
    """
    
    # calculate the uniform pdf
    if not isinstance(r, (list, tuple, np.ndarray)):
        return 1/(b-a) if r >= a and r <= b else 0
    else:
        return [1/(b-a) if i >= a and i <= b else 0 for i in r]
    
def plot_uniform_pdf(a:float,
                     b:float,
                     x_min:float=0,
                     x_max:float=5,
                     num_points:int=1000
                    ) -> None:
    """
    Plots the uniform pdf.

    Parameters
    - a: lower limit of the pdf
    - b: upper limit of the pdf
    - x_min: least value to plot on the x-axis
    - x_max: max value to plot on the x-axis
    - num_points: number of points to calculate and plot
    """
    uniform_pdf_func = partial(uniform_pdf, a=a, b=b)
    plot_2d_function(uniform_pdf_func, x_min, x_max, num_points, 'Uniform p.d.f.')

def exp_pdf(r:float|list, rate:float) -> float|list:
    """
    Calculates the Exponential p.d.f.

    Parameters:
    - r: the independent variable
    - rate: lambda parameter of the exponential pdf
    """
    return rate * np.exp(-rate * r)

def plot_exp_pdf(rate:float,
                 x_min:float=0,
                 x_max:float=5,
                 num_points:int=1000
                ) -> None:
    """
    Plots the exponential pdf.

    Parameters
    - rate: lambda parameter of the exponential pdf
    - x_min: least value to plot on the x-axis
    - x_max: max value to plot on the x-axis
    - num_points: number of points to calculate and plot
    """
    exp_pdf_func = partial(exp_pdf, rate=rate)
    exp_pdf_func.__name__ = f"$\lambda={rate}$"
    plot_2d_function(exp_pdf_func, x_min, x_max, num_points, 'Exponential p.d.f.')

def doubly_exp_pdf(r:float|list, rate:float) -> float|list:
    """
    Calculates the Doubly Exponential p.d.f.

    Parameters:
    - r: the independent variable
    - rate: lambda parameter of the doubly exponential pdf
    """
    return rate/2 * np.exp(-rate * abs(r))

def plot_doubly_exp_pdf(rate:float,
                        x_min:float=-5,
                        x_max:float=5,
                        num_points:int=1000
                        ) -> None:
    """
    Plots the doubly exponential pdf.

    Parameters
    - rate: lambda parameter of the exponential pdf
    - x_min: least value to plot on the x-axis
    - x_max: max value to plot on the x-axis
    - num_points: number of points to calculate and plot
    """
    exp_pdf_func = partial(doubly_exp_pdf, rate=rate)
    exp_pdf_func.__name__ = f"$\lambda={rate}$"
    plot_2d_function(exp_pdf_func, x_min, x_max, num_points, 'Doubly Exponential p.d.f.')