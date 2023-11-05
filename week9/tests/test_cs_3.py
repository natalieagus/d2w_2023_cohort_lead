import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from source.cs_3 import predict_linreg
from source.cs_1 import prepare_target 
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

def test_cs_3(df_feature_df_target):

    df_feature, df_target = df_feature_df_target
    beta = [[22.53279993],[ 6.39529594]] # from previous result
    pred = predict_linreg(df_feature, beta)

    assert isinstance(pred, np.ndarray)
    assert pred.shape == (506, 1)
    assert np.isclose(pred.mean(), 22.5328)
    assert np.isclose(pred.std(), 6.38897)

    means = [6.284634]
    stds = [0.702617]
    beta = [[22.53279993],[ 6.39529594]] # from previous result
    input_1row = np.array([[6.593]])
    pred_1row = predict_linreg(input_1row, beta, means, stds)
    assert np.isclose(pred_1row[0][0], 25.33958)
    target = prepare_target(df_target)
    
    if (pytest.plot_output):
        plt.plot(df_feature["RM"],target,'o')
        plt.plot(df_feature["RM"],pred,'-')  
        plt.show()  