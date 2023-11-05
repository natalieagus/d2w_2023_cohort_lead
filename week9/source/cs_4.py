import numpy as np
import matplotlib.pyplot as plt
from .cs_0 import get_features_targets, normalize_z
from .cs_1 import prepare_feature, prepare_target
from .cs_2 import gradient_descent_linreg
from .cs_3 import predict_linreg 

def split_data(df_feature, df_target, random_state=None, test_size=0.5):
    ### BEGIN SOLUTION
    indexes = df_feature.index
    # rng = np.random.default_rng()
    if random_state != None:
        np.random.seed(random_state)
        # rng = np.random.default_rng(seed=random_state)
    k = int(test_size * len(indexes))
    test_index = np.random.choice(indexes, k, replace=False)
    # test_index = rng.choice(indexes, k, replace=False)
    indexes = set(indexes)
    test_index = set(test_index)
    train_index = indexes - test_index
    test_index_list = list(test_index) # using set as indexer in pandas loc will be deprecated soon
    train_index_list = list(train_index)
    df_feature_train = df_feature.loc[train_index_list, :]
    df_feature_test = df_feature.loc[test_index_list, :]
    df_target_train = df_target.loc[train_index_list, :]
    df_target_test = df_target.loc[test_index_list, :]
    ### END SOLUTION
    return df_feature_train, df_feature_test, df_target_train, df_target_test

    