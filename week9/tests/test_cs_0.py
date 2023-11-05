import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from source.cs_0 import get_features_targets, normalize_z 
import matplotlib.pyplot as plt
import seaborn as sns
import pytest 

def test_cs_0(df_data_object):
    df = df_data_object
    df_feature, df_target = get_features_targets(df,["RM"],["MEDV"])
    df_feature,_,_ = normalize_z(df_feature)

    assert isinstance(df_feature, pd.DataFrame)
    assert isinstance(df_target, pd.DataFrame)
    assert np.isclose(df_feature.mean(), 0.0)
    assert np.isclose(df_feature.std(), 1.0)
    assert np.isclose(df_target.mean(), 22.532806)
    assert np.isclose(df_target.std(), 9.1971)

    if (pytest.plot_output):
        sns.set()
        plt.scatter(df_feature, df_target)   
        plt.show()