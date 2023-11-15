import numpy as np
from source.cs_2 import compute_cost_logreg
from source.cs_1 import calc_logreg


def gradient_descent_logreg(X, y, beta, alpha, num_iters):
    """
    Perform gradient descent for logistic regression.

    Parameters:
    - X (numpy.ndarray): Matrix of size # samples * # parameters.
    - y (numpy.ndarray): Actual target values, a column vector of size # samples.
    - beta (numpy.ndarray): Column vector of size # parameters representing the coefficients.
    - alpha (float): Learning rate for gradient descent.
    - num_iters (int): Number of iterations for gradient descent.

    Returns:
    tuple: A tuple containing two elements:
        - numpy.ndarray: Updated beta vector.
        - numpy.ndarray: 1D array of J_storage storing the error at each iteration of gradient descent.

    Notes:
    - The input X is a matrix of size # samples * # parameters.
    - The input y is a column vector of size # samples.
    - The input beta is a column vector of size # parameters.
    - The learning rate (alpha) controls the step size in the gradient descent algorithm.
    - The number of iterations (num_iters) determines how many times the algorithm will update beta.
    - The function returns a tuple with the updated beta vector and an array of errors (J_storage) at each iteration.
    """
    number_of_samples = X.shape[0]
    # Prepare an array to store errors
    # An array of zeroes, with dimensions of # iters times 1 (it's a 1D array)
    J_storage = np.zeros((num_iters, 1))
    for n in range(num_iters):
        # Update beta repeatedly
        # Compute derivative of error with respect to current beta
        derivative = np.matmul(X.T, (calc_logreg(X, beta) - y))
        # Update beta
        beta = beta - alpha * (1 / number_of_samples) * derivative
        # Store the current error
        J_storage[n] = compute_cost_logreg(beta, X, y)

    return beta, J_storage
