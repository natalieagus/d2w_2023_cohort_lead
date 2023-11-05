import numpy as np
import pandas as pd
from source.cs_5 import r2_score

def test_cs_5(target_pred):
    target, pred = target_pred
    r2 = r2_score(target, pred)
    assert np.isclose(r2, 0.45398)