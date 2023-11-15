import numpy as np
from source.cs_3 import gradient_descent_logreg

try:
    from source.cs_0 import feature, target
except:
    print("cs_0 not implemented yet")

import matplotlib.pyplot as plt
import pytest


def test_cs_3():
    iterations = 1500
    alpha = 0.01
    beta = np.zeros((2, 1))
    beta, J_storage = gradient_descent_logreg(feature, target, beta, alpha, iterations)

    assert beta.shape == (2, 1)
    assert np.isclose(beta[0][0], -0.56630)
    assert np.isclose(beta[1][0], 1.93764)

    if pytest.plot_output:
        plt.plot(J_storage)
        plt.show()
