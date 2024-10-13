# mathlib/plotting.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import Callable, List, Union

plot_theme = 'dark_background'

def plot_2d_function(
    functions: Union[Callable[[np.ndarray], np.ndarray], List[Callable[[np.ndarray], np.ndarray]]],
    x_min: float = -10,
    x_max: float = 10,
    num_points: int = 1000,
    title: str = '2D Plot of Functions',
    plot_theme: str = 'dark_background'
) -> None:
    """
    Plots 2D graphs of one or more functions f(x) vs x on the same plot.

    Parameters:
    - functions: A single function or a list of functions to plot (each callable that takes x as input).
    - x_min: Minimum value of x (default: -10).
    - x_max: Maximum value of x (default: 10).
    - num_points: Number of points in the graph (default: 1000).
    - title: Title at the top of the plot (default: '2D Plot of Functions').
    - plot_theme: Matplotlib theme to use (default: 'dark_background').
    """
    # Ensure functions is a list even if a single function is passed
    if not isinstance(functions, (list, tuple)):
        functions = [functions]
    
    # Generate x values
    x = np.linspace(x_min, x_max, num_points)

    # Set the style to the specified theme
    plt.style.use(plot_theme)
    
    # Create a figure for plotting
    plt.figure()

    # Plot each function
    for f in functions:
        y = f(x)
        plt.plot(x, y, label=f.__name__ if hasattr(f, '__name__') else 'f(x)')
    
    # Add title, labels, and grid
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    
    # Add legend to distinguish between functions
    plt.legend()

    # Show the plot
    plt.show()


def plot_3d_function(f, x_min=-10, x_max=10, y_min=-10, y_max=10, num_points=100):
    """
    Plots a 3D surface graph of f(x, y) vs x and y.
    
    Parameters:
    - f: Function to plot (callable that takes x and y as input).
    - x_min: Minimum value of x (default: -10).
    - x_max: Maximum value of x (default: 10).
    - y_min: Minimum value of y (default: -10).
    - y_max: Maximum value of y (default: 10).
    - num_points: Number of points in the graph (default: 100).
    """
    x = np.linspace(x_min, x_max, num_points)
    y = np.linspace(y_min, y_max, num_points)
    x, y = np.meshgrid(x, y)
    z = f(x, y)

    # Set the style to 'dark_background'
    plt.style.use(plot_theme)
    
    # Plot the function
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_title("3D Plot of f(x, y)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")

    plt.show()

def plot_bar_chart(
        names: List[str],
        data: List[float],
        title: str = "Bar Chart",
        x_label: str = "Categories",
        y_label: str = "Values",
        plot_theme: str = "dark_background"
    ) -> None:
    """
    Plots a bar chart where the x-axis represents the names (categories) and the y-axis represents the data values.

    Parameters:
    - names: List of names (categories) for the x-axis.
    - data: List of data values corresponding to each name.
    - title: Title of the bar chart (default: "Bar Chart").
    - x_label: Label for the x-axis (default: "Categories").
    - y_label: Label for the y-axis (default: "Values").
    - plot_theme: Matplotlib theme to use (default: 'dark_background').
    """
    if len(names) != len(data):
        raise ValueError("The length of 'names' and 'data' must be the same.")

    # Set the style to the specified theme
    plt.style.use(plot_theme)
    
    # Create the bar chart
    plt.figure()
    plt.bar(names, data)

    # Set the title and axis labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # Display the grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.show()

def plot_histogram(data: List[float], bins: int = 10, title: str = "Histogram", x_label: str = "Values", y_label: str = "Frequency", plot_theme: str = "dark_background") -> None:
    """
    Plots a histogram to show the distribution of the data.

    Parameters:
    - data: A list of numerical data points to plot in the histogram.
    - bins: Number of bins (intervals) for the histogram (default: 10).
    - title: Title of the histogram (default: "Histogram").
    - x_label: Label for the x-axis (default: "Values").
    - y_label: Label for the y-axis (default: "Frequency").
    - plot_theme: Matplotlib theme to use (default: 'dark_background').
    """
    # Set the style to the specified theme
    plt.style.use(plot_theme)
    
    # Create the histogram
    plt.figure()
    plt.hist(data, bins=bins, edgecolor='white')  # edgecolor for better separation between bins

    # Set the title and axis labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # Display the grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.show()