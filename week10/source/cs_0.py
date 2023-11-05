import pandas as pd
import numpy as np

def normalize_z(dfin, columns_means=None, columns_stds=None):
    ###BEGIN SOLUTION
    if columns_means is None:
        columns_means = dfin.mean(axis=0)
    if columns_stds is None:
        columns_stds = dfin.std(axis=0)
    dfout = (dfin - np.array(columns_means)) / np.array(columns_stds)
    ###END SOLUTION 
    return dfout, columns_means, columns_stds

def get_features_targets(df, feature_names, target_names):
    ### BEGIN SOLUTION
    df_feature = df[feature_names]
    df_target = df[target_names]
    ### END SOLUTION
    pass
    return df_feature, df_target

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

def split_data(df_feature, df_target, random_state=None, test_size=0.5):
    ### BEGIN SOLUTION
    indexes = df_feature.index
    if random_state != None:
        np.random.seed(random_state)
    k = int(test_size * len(indexes))
    test_index = np.random.choice(indexes, k, replace=False)
    indexes = set(indexes)
    test_index = set(test_index)
    train_index = indexes - test_index
    df_feature_train = df_feature.loc[train_index, :]
    df_feature_test = df_feature.loc[test_index, :]
    df_target_train = df_target.loc[train_index, :]
    df_target_test = df_target.loc[test_index, :]
    ### END SOLUTION
    return df_feature_train, df_feature_test, df_target_train, df_target_test


## TASK 2
df = pd.read_csv('./data/breast_cancer_data.csv')

## TASK 3
df_feature, df_target = get_features_targets(df, ["radius_mean"], ["diagnosis"])
df_feature,_,_ = normalize_z(df_feature)
## TASK 4
def replace_target(df_target, target_name, map_vals):
    ### BEGIN SOLUTION
    df_out = df_target.copy()

    df_out.loc[:, target_name] = df_target[target_name].apply(lambda x: map_vals[x])
    ### END SOLUTION
    return df_out
df_target = replace_target(df_target, "diagnosis", {'M': 1, 'B': 0})

## TASK 5
feature = prepare_feature(df_feature)
target = prepare_target(df_target)
