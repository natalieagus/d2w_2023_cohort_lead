import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from source.cs_2 import gradient_descent_linreg
import matplotlib.pyplot as plt
import seaborn as sns
import pytest 

def test_cs_2(x_z_target):
    X, target = x_z_target 
    iterations = 1500
    alpha = 0.01
    beta = np.zeros((2,1))

    beta, J_storage = gradient_descent_linreg(X, target, beta, alpha, iterations)
    assert np.isclose(beta[0], 22.5328)
    assert np.isclose(beta[1], 6.3953)

    if (pytest.plot_output):
        plt.plot(J_storage)
        plt.show()    