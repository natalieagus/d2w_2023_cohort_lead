import numpy as np


def calc_logreg(X, beta):
    """
    Calculate the logistic regression output.

    Parameters:
    - X (numpy.ndarray): A matrix of size # samples * # of parameters,
      where each row represents a sample and each column represents a parameter.
    - beta (numpy.ndarray): A vector of size # of parameters, representing the coefficients.

    Returns:
    numpy.ndarray: The logistic regression output as a column vector.

    Note:
    - The argument types must be numpy arrays.
    - The output is a column vector, for example, [[1], [2], [3]].
    - The number of parameters is determined by the number of features plus 1.
    - The logistic regression output is calculated using the sigmoid function:
      output = 1 / (1 + exp(-X @ beta))
    """
    return 1 / (1 + np.exp(np.matmul(X, -beta)))
