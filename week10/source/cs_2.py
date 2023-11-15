import numpy as np
from source.cs_1 import calc_logreg


def compute_cost_logreg(beta, X, y):
    """
    Compute the cost for logistic regression.

    Parameters:
    - beta (numpy.ndarray): Column vector of size # parameters representing the coefficients.
    - X (numpy.ndarray): Matrix of size # samples * # parameters, where each row is a sample,
      and each column is a parameter.
    - y (numpy.ndarray): Actual target values, a column vector of size # samples.

    Returns:
    float: The computed cost for logistic regression.

    Notes:
    - The input X is a matrix of size # samples * # parameters.
    - The input beta is a column vector of size # parameters.
    - The input y is a column vector of size # samples.
    - The cost is computed using the logistic regression formula:
      J = -(1 / m) * sum(y * log(h(X, beta)) + (1 - y) * log(1 - h(X, beta)))
      where h(X, beta) is the logistic regression output.
    """
    number_of_samples = len(y)
    J = -(1 / number_of_samples) * np.sum(
        np.where(y == 1, np.log(calc_logreg(X, beta)), np.log(1 - calc_logreg(X, beta)))
    )
    return J
