import numpy as np 
from source.cs_2 import compute_cost_logreg
from source.cs_1 import calc_logreg

def gradient_descent_logreg(X, y, beta, alpha, num_iters):
    ### BEGIN SOLUTION
    m = X.shape[0]
    J_storage = np.zeros((num_iters, 1))
    for n in range(num_iters):
        deriv = np.matmul(X.T, (calc_logreg(X, beta) - y))
        beta = beta - alpha * (1 / m) * deriv
        J_storage[n] = compute_cost_logreg(beta, X, y)
    ### END_SOLUTION 
    return beta, J_storage
    
