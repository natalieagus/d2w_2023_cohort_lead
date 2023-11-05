from source.cs_0 import normalize_z 
from source.cs_1 import prepare_feature, calc_linreg


def predict_linreg(df_feature, beta, means=None, stds=None):
    ### BEGIN SOLUTION
    norm_data, _,_ = normalize_z(df_feature, means, stds)
    X = prepare_feature(norm_data)
    return calc_linreg(X, beta)
    ### END SOLUTION
    pass