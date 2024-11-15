import numpy as np

def log_map1_demo(y0 = 0.5, max_iterations = 300, resolution = 500) -> np.ndarray:
    data = orbit_diagram(y0, max_iterations, resolution)
    return data

def orbit_diagram(y0, max_iter, resolution) -> np.ndarray:
    """

    :param y0: the initial value of y — The "base case" for the recursive function called for each c in c_range.
            Can be in range from -0.5 to 0.5
    :param max_iter: the maximum number of iterations to prevent infinite recursion.
            Optimal values are roughly in range from 20 to 995(cutoff)
    :param resolution: the number of points to generate in the range of c (which is in range from -2 to 0.25).
            For each of those points the values of the function will be generated.
            The higher the resolution, the more detailed the diagram.
    :return: a numpy array of the data points generated for the orbit diagram.
    """
    data = []
    # This code restricts the range of c to [-2, 0.25], which prevents overflow errors.
    c_range = np.linspace(-2, 0.25, resolution)
    for c in c_range:
        orbit_diagram_slice(y0, c, max_iter, data)
    data = np.array(data)
    return data


def orbit_diagram_slice(y0, c, max_iter, data):

    if max_iter > 0:
        # c += 0.0001
        y = pow(y0, 2) + c
        data.append((y0, c))
        return orbit_diagram_slice(y, c, max_iter - 1, data)
    return y0
