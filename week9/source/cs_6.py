import numpy as np 

def mean_squared_error(target, pred):
    ### BEGIN SOLUTION
    n = target.shape[0]
    #return (1/n)*np.sum((target - pred)**2)
    error = target-pred
    return (1 / n) * np.matmul(error.T, error)[0][0]
    ### END SOLUTION
    pass