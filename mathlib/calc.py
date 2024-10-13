# mathlib/calc.py

def integrate(f, x_min:float, x_max:float, dx:float):
    """
    Integrate the function f(x) using a Riemann's sum.

    Parameters:
    - f: the function f(x) to integrate
    - x_min: the lower bound of the integration
    - x_max: the upper bound of the integration
    - dx: the width to segment the area under the curve
    """

    # initialize running variables
    running_sum = 0
    x = x_min

    # calculate the area at each f(x) as f(x)dx
    while(x < x_max):
        running_sum += f(x)*dx
        x += dx
    
    return running_sum
