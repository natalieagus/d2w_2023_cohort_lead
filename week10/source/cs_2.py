import numpy as np 
from source.cs_1 import calc_logreg

def compute_cost_logreg(beta, X, y):
    np.seterr(divide = 'ignore') 
    ### BEGIN SOLUTION
    m = len(y)
    J = -(1/m)*np.sum(np.where(y==1, np.log(calc_logreg(X, beta)),np.log(1-calc_logreg(X, beta))))
    
    ### END SOLUTION
    np.seterr(divide = 'warn')
    return J