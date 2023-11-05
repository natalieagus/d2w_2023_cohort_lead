import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from source.cs_1 import prepare_feature, prepare_target, compute_cost_linreg


def test_cs_1(df_feature_z_df_target):
    df_feature, df_target = df_feature_z_df_target

    X = prepare_feature(df_feature)
    target = prepare_target(df_target)

    assert isinstance(X, np.ndarray)
    assert isinstance(target, np.ndarray)
    assert X.shape == (506, 2)
    assert target.shape == (506, 1)

    # print(X)
    beta = np.zeros((2,1))
    J = compute_cost_linreg(X, target, beta)
    # print(J)
    assert np.isclose(J, 296.0735)

    beta = np.ones((2,1))
    J = compute_cost_linreg(X, target, beta)
    # print(J)
    assert np.isclose(J, 268.157)

    beta = np.array([-1, 2]).reshape((2,1))
    J = compute_cost_linreg(X, target, beta)
    # print(J)
    assert np.isclose(J, 308.337)