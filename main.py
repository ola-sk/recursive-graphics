import matplotlib.pyplot as plt

from logistic_map1 import log_map1_demo
from logistic_map2 import log_map2_demo

if __name__ == "__main__":
    # Generate the orbit diagram for the logistic map
    # Set up parameters for the orbit diagram
    data = log_map1_demo()
    plt.scatter(data[:, 1], data[:, 0], s=0.003)
    plt.show()

    data = log_map2_demo()
    plt.scatter(data[:, 1], data[:, 0], s=0.003)
    plt.show()