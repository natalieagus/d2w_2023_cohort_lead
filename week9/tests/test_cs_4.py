import numpy as np
import pandas as pd

from source.cs_4 import split_data
from source.cs_0 import get_features_targets, normalize_z
from source.cs_1 import prepare_feature, prepare_target
from source.cs_2 import gradient_descent_linreg
from source.cs_3 import predict_linreg
import matplotlib.pyplot as plt
import pytest 

def test_cs_4(df_data_object):
    df = df_data_object 
    
    ### BEGIN SOLUTION 
    df_feature, df_target = get_features_targets(df, ["RM"], ["MEDV"])
    df_feature_train, df_feature_test, df_target_train, df_target_test = split_data(df_feature, df_target, random_state=100, test_size=0.3)
    df_feature_train_z,_,_ = normalize_z(df_feature_train)
    X = prepare_feature(df_feature_train_z)
    target = prepare_target(df_target_train)

    iterations = 1500
    alpha = 0.01
    beta = np.zeros((2,1))
    beta, _ = gradient_descent_linreg(X, target, beta, alpha, iterations)
    pred = predict_linreg(df_feature_test, beta)
    ### END SOLUTION
    
    assert isinstance(pred, np.ndarray)
    assert pred.shape == (151, 1)
    assert np.isclose(pred.mean(), 22.66816)
    assert np.isclose(pred.std(), 6.257265)

    if (pytest.plot_output):
        plt.scatter(df_feature_test, df_target_test)
        plt.plot(df_feature_test, pred, color="orange")   
        plt.show() 