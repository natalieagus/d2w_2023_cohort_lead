import numpy as np 
from source.cs_2 import calc_logreg
from source.cs_0 import normalize_z, prepare_feature

def predict_norm(X, beta):
    ### BEGIN SOLUTION
    p = calc_logreg(X, beta)
    return np.where(p >= 0.5, 1, 0)
    ### END SOLUTION
    pass

def predict_logreg(df_feature, beta, means=None, stds=None):
    ### BEGIN SOLUTION
    norm_data, _, _ = normalize_z(df_feature, means, stds)
    X = prepare_feature(norm_data)
    return predict_norm(X, beta)
    ### END SOLUTION
    pass