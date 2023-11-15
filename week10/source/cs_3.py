import numpy as np
from source.cs_2 import compute_cost_logreg
from source.cs_1 import calc_logreg


# input parameters are X matrix, np array, then beta parameters (column vector), alpha and num_iters are float and int respectively
# y is the actual target, which is also a column vector
# return a tuple of two things: beta vector, and the 1D array of J_storage storing the error at each iteration of gradient descent
def gradient_descent_logreg(X, y, beta, alpha, num_iters):
    number_of_samples = X.shape[0]
    # prepare an array to store errors
    # an array of zeroes, with dimension of # iters times 1 (it's a 1D array)
    J_storage = np.zeros((num_iters, 1))
    for n in range(num_iters):
        # update beta repeatedly
        # compute derivate of error wrt current beta
        derivative = np.matmul(X.T, (calc_logreg(X, beta) - y))
        # update beta
        beta = beta - alpha * (1 / number_of_samples) * derivative
        # store the current error
        J_storage[n] = compute_cost_logreg(beta, X, y)

    return beta, J_storage
