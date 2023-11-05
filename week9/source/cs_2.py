import numpy as np 
# When you use from .cs_1, you are specifying cs_1 relative import within the current package, indicating that you want to import cs_1.py from the same directory/package where cs_2.py (this file) is 
from source.cs_1 import compute_cost_linreg, calc_linreg

def gradient_descent_linreg(X, y, beta, alpha, num_iters):
    ### BEGIN SOLUTION
    m = X.shape[0]
    J_storage = np.zeros((num_iters, 1))
    for n in range(num_iters):
        deriv = np.matmul(X.T, (calc_linreg(X, beta) - y))
        beta = beta - alpha * (1 / m) * deriv
        J_storage[n] = compute_cost_linreg(X, y, beta)
    ### END SOLUTION
    return beta, J_storage