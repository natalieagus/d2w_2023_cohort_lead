import numpy as np 
from source.cs_1 import calc_logreg

def test_cs_1():
    beta = np.array([0])
    x = np.array([0])
    ans = calc_logreg(x, beta)
    assert np.isclose(ans, 0.5, rtol=1e-09, atol=1e-09)

    beta = np.array([2])
    x = np.array([40])
    ans = calc_logreg(x, beta)
    assert np.isclose(ans, 1.0)

    beta = np.array([2])
    x = np.array([-40])
    ans = calc_logreg(x, beta)
    assert np.isclose(ans, 0.0)

    beta = np.array([[1, 2, 3]])
    x = np.array([[3, 2, 1]])
    ans = calc_logreg(x, beta.T)
    assert np.isclose(ans.all(), 1.0)

    beta = np.array([[1, 2, 3]])
    x = np.array([[3, 2, 1], [3, 2, 1]])
    ans = calc_logreg(x, beta.T)
    assert ans.shape == (2, 1)
    assert np.isclose(ans.all(), 1.0)