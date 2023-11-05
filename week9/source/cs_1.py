import numpy as np 
import pandas as pd 

def calc_linreg(X, beta):
    ### BEGIN SOLUTION
    return np.matmul(X, beta)
    ### END SOLUTION
    pass

def compute_cost_linreg(X, y, beta):
    J = 0
    ### BEGIN SOLUTION
    m = X.shape[0]
    error = calc_linreg(X, beta) - y
    error_sq = np.matmul(error.T, error)
    J = (1/(2 * m)) * error_sq
    J = J[0][0]
    ### END SOLUTION
    return J


def prepare_feature(df_feature):
    ### BEGIN SOLUTION
    # cols = len(df_feature.columns)
    cols = df_feature.shape[1]
    if type(df_feature) == pd.DataFrame:
        np_feature = df_feature.to_numpy()
    else:
        np_feature = df_feature
    feature = np_feature.reshape(-1, cols)
    X = np.concatenate((np.ones((feature.shape[0],1)), feature), axis=1)
    return X
    ### END SOLUTION
    pass

def prepare_target(df_target):
    ### BEGIN SOLUTION
    # cols = len(df_target.columns)
    cols = df_target.shape[1]
    if type(df_target) ==  pd.DataFrame:
        np_target = df_target.to_numpy()
    else:
        np_target = df_target
    target = np_target.reshape(-1, cols)
    return target
    ### END SOLUTION
    pass