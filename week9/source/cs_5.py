import numpy as np 
def r2_score(y, ypred):
    ### BEGIN SOLUTION
    ymean = np.mean(y)
    diff = y - ymean
    #sstot = np.sum((y - ymean)**2)
    sstot = np.matmul(diff.T, diff)
    #ssres = np.sum((y - ypred)**2)
    error = y - ypred
    ssres = np.matmul(error.T, error)
    return 1 - (ssres/sstot)[0][0]
    ### END SOLUTION
    pass

