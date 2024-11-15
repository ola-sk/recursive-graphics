import numpy as np

def log_map2_demo(y0 = 0.01, max_iterations = 300, resolution = 700) -> np.ndarray:
    data = orbit_diagram(y0, max_iterations, resolution)
    return data

def orbit_diagram(y0, max_iter, resolution) -> np.ndarray:
    """

    :param y0: the initial value of y — The "base case" for the recursive function called for each r in r_range.
            Can be in range from 0 to 1.
    :param max_iter:  the maximum number of iterations to prevent infinite recursion.
            Optimal values are roughly in range from 20 to 995(cutoff)
    :param resolution: the number of points to generate in the range of r (from 0 to 4)
            for which the diagram will be generated.
    :return: a numpy array of the data points generated for the orbit diagram.
    """

    data = []
    # This code restricts the range of r to [-2, 4], which prevents overflow errors.
    # the range can be adjusted to get different "portion" of the graph (without calculating the rest).
    r_range = np.linspace(-2, 4, resolution)
    for r in r_range:
        orbit_diagram_slice(y0, r, max_iter, data)
    data = np.array(data)
    return data

def orbit_diagram_slice(y0, r, max_iter, data):
    """
    :param y0: the initial value of y — The "base case". Range from 0 to 1.
    :param r: the parameter for the logistic map
    :param max_iter: the maximum number of iterations
    :param data: the list to store the data points
    :return: the final value of y after max_iter iterations
    """
    data.append((y0, r))
    if max_iter > 0:
        y = r * y0 * (1 - y0)
        return orbit_diagram_slice(y, r, max_iter - 1, data)
    return y0

# Incorporating sigmoid function to smooth out things?
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))



