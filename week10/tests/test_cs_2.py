import numpy as np 
from source.cs_2 import compute_cost_logreg 

def test_cs_2():
    y = np.array([[1]])
    X = np.array([[10, 40]])
    beta = np.array([[1, 1]]).T
    ans = compute_cost_logreg(beta, X, y)
    assert np.isclose(ans, 0)

    y = np.array([[0]])
    X = np.array([[10, 40]])
    beta = np.array([[-1, -1]]).T
    ans = compute_cost_logreg(beta, X, y)
    assert np.isclose(ans, 0)
