import numpy as np
import matplotlib.pyplot as plt
from .cs_0 import get_features_targets, normalize_z
from .cs_1 import prepare_feature, prepare_target
from .cs_2 import gradient_descent_linreg
from .cs_3 import predict_linreg


def split_data(df_feature, df_target, random_state=None, test_size=0.5):
    # seed the random generator first
    if random_state != None:
        np.random.seed(random_state)

    # check how many samples I have? Get the indexes of features (or target)
    indexes = df_feature.index
    # I want to select random indexes to form my test set
    # what proportion of the indexes can be used as test set?
    test_set_proportion = int(
        test_size * len(indexes)
    )  # test_size is a value between 0 to 1
    # eg: indexes  is [0, 1, 2, 3, 4, 5]
    # test_set_proportion is 3
    # then test_index will be 3 elements selected out from indexes randomly, eg: [2, 4, 5]
    test_index = np.random.choice(indexes, test_set_proportion, replace=False)

    # now we have test_index, we need to get train_index
    # train_index should be [0, 1, 3]
    # we cannot just subtract lists together to get the above, but we can subtract sets (python sets)
    indexes = set(indexes)
    test_index = set(test_index)
    train_index = indexes - test_index

    # prepare test set
    df_feature_test = df_feature.loc[
        test_index, :
    ]  # select rows with test_index, and all columns
    df_target_test = df_target.loc[test_index, :]

    # prepare train set
    df_feature_train = df_feature.loc[train_index, :]
    df_target_train = df_target.loc[train_index, :]

    return df_feature_train, df_feature_test, df_target_train, df_target_test
