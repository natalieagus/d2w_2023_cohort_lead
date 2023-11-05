
import numpy as np 
from source.cs_4 import predict_logreg
from source.cs_0 import df_feature, df_target
import matplotlib.pyplot as plt
import pytest 

def test_cs_4():
    beta = np.array( [[-0.56630289], [1.93763591]] )
    pred = predict_logreg(df_feature, beta)
    assert isinstance(pred, np.ndarray)
    assert np.isclose(pred.mean(), 0.28998)
    assert np.isclose(pred.std(), 0.45375)

    means = [0]
    stds = [1]
    beta =np.array([[-0.56630289], [ 1.93763591]])
    input_1row = np.array([[2.109139]])
    pred_1row = predict_logreg(input_1row, beta, means, stds)
    assert pred_1row[0][0] == 1

    if (pytest.plot_output):
        plt.scatter(df_feature, df_target)
        plt.scatter(df_feature, pred)
        plt.show()