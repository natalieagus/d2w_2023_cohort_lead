import numpy as np
import pandas as pd


def calc_linreg(X, beta):
    # X is a matrix of dimension # samples * # parameters
    # beta is vector of dimension # parameters * 1
    # output should be y hat vector having dimension of # samples * 1
    return np.matmul(X, beta)
    pass


def compute_cost_linreg(X, y, beta):
    # check that y is np array
    # computing value of J
    # X is the feature matrix, y is actual target
    J = 0
    num_of_samples = X.shape[0]  # # of rows is # samples
    y_hat_vector = calc_linreg(X, beta)
    error = y_hat_vector - y  # a vector dimension # samples * 1
    sum_error_sq = np.matmul(error.T, error)
    J = 1 / (2 * num_of_samples) * sum_error_sq  # J has only 1 value, but its a 2darray
    # this function should return a scalar
    return J[0][0]


# df_feature can be a df, or a numpy array
def prepare_feature(df_feature):
    # big X must be returned here
    # dimension of: # of samples x # of parameters
    cols = df_feature.shape[1]  # get # features in case we have more than 1
    if type(df_feature) == pd.DataFrame:
        np_feature = df_feature.to_numpy()
    else:
        np_feature = df_feature
    feature = np_feature.reshape(
        -1, cols
    )  # reshape to ensure that we have the same cols as before

    # np.ones((feature.shape[0], 1)) returns a column vector of 1s for as many as feature.shape[0] rows
    # [[1], [1], [1], ...., [1]]
    # feature = [[3], [5], [23], ... [9]]
    # X = [ [1,3], [1, 5], [1, 23], ... [1,9]]
    X = np.concatenate((np.ones((feature.shape[0], 1)), feature), axis=1)
    pass


# the target is basically y --> dependent variable
# this is a column vector, with rows as many as #samples
def prepare_target(df_target):
    cols = df_target.shape[
        1
    ]  # df_target.shape returns a tuple #row,#col, i'm expecting 1 here at Week 9

    # check if df_target is a dataframe?
    if type(df_target) == pd.DataFrame:
        # if yes, convert to numpy using the to_numpy() func from Pandas
        np_target = df_target.to_numpy()
    else:
        # by definition, if arg is not a DF, it will be a numpy array
        np_target = df_target
    # ensure that we return a vector for each target
    return np_target.reshape(-1, cols)
