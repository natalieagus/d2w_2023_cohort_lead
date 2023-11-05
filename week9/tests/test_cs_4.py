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

    ## TODO 
    beta, pred, df_feature_test, df_target_test = None 
    
    
    assert isinstance(pred, np.ndarray)
    assert pred.shape == (151, 1)
    assert np.isclose(pred.mean(), 22.66816)
    assert np.isclose(pred.std(), 6.257265)

    if (pytest.plot_output):
        plt.scatter(df_feature_test, df_target_test)
        plt.plot(df_feature_test, pred, color="orange")   
        plt.show() 