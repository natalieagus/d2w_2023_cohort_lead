import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from source.cs_6 import mean_squared_error

def test_cs_6(target_pred):
    target, pred = target_pred
    mse = mean_squared_error(target, pred)
    assert np.isclose(mse, 53.6375)