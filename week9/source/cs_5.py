import numpy as np


def r2_score(y, ypred):
    ymean = np.mean(y)  # get the actual mean
    # get the diff between the target and its actual mean
    diff = y - ymean
    # ss_tot is the square diff
    ss_tot = np.matmul(diff.T, diff)
    error = y - ypred  # this is how far away our pred y (yhat) from actual target
    # ss_res is the square error
    ss_res = np.matmul(error.T, error)
    return (
        1 - (ss_res / ss_tot)[0][0]
    )  # remember to return an element, not a matrix of 1 element
