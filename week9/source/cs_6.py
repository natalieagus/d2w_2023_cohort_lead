import numpy as np


def mean_squared_error(target, pred):
    error = target - pred  # find the diff between y and yhat, this is our error
    sq_error = np.matmul(error.T, error)  # dont forget, this a matrix with 1 element
    # get the mean of the sq error and return
    return (1 / target.shape[0]) * sq_error[0][0]
