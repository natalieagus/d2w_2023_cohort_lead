import numpy as np 

def calc_logreg(X, beta):
    ### BEGIN SOLUTION
    #print(X.shape, beta.shape)
    return 1/(1 + np.exp(np.matmul(X, -beta)))
    #return 1/(1 + np.exp(np.matmul(-beta.T,X.T).T))
    ### END SOLUTION
    pass