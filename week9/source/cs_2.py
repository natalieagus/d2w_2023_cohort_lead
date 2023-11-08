import numpy as np
from source.cs_1 import compute_cost_linreg, calc_linreg


def gradient_descent_linreg(X, y, beta, alpha, num_iters):
    num_of_samples = X.shape[0]
    # prepare an array to compute J at each iteration (error), want to see if it's decreasing eventually with every iteration of gradient descent
    J_storage = np.zeros((num_iters, 1))  # this for illustration purposes
    for n in range(num_iters):
        current_derivative = np.matmul(X.T, (calc_linreg(X, beta) - y))
        # beta updates
        beta = beta - alpha * (1 / num_of_samples) * current_derivative
        # check the amount of error now
        J_storage[n] = compute_cost_linreg(X, y, beta)

    return beta, J_storage
