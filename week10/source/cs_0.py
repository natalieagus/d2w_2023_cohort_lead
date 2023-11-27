import pandas as pd
import numpy as np
import os

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
    X = np.concatenate((np.ones((feature.shape[0], 1)), feature), axis=1)
    return X
    ### END SOLUTION
    pass


def prepare_target(df_target):
    ### BEGIN SOLUTION
    # cols = len(df_target.columns)
    cols = df_target.shape[1]
    if type(df_target) == pd.DataFrame:
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


current_directory = os.getcwd()

# Check if the "week10" directory is one level above the current directory
if os.path.basename(current_directory) == "week10":
    # If the script is in the "week10 directory
    file_path = os.path.join(current_directory, "data", "breast_cancer_data.csv")
else:
    # If the script is one level above the "week10" directory
    file_path = os.path.join(
        current_directory, "week10", "data", "breast_cancer_data.csv"
    )


## TASK 2
df = pd.read_csv(file_path)

## TASK 3
df_feature, df_target = get_features_targets(df, ["radius_mean"], ["diagnosis"])
# normalise feature because we only care about relative values between the features and not the absolute value
df_feature, _, _ = normalize_z(df_feature)


## TASK 4
def replace_target(df_target, target_name, map_vals):
    df_out = (
        df_target.copy()
    )  # make a copy of the original target df that contains "m"  and "b"  as values
    # replace the column matching target_name, e.g: "diagnosis", and apply a function over its elements
    # x represents every element in diagnosis column, which is x can be 'M' or x can be 'B'
    df_out.loc[:, target_name] = df_target[target_name].apply(lambda x: map_vals[x])

    return df_out
    pass


# use the function above
map_values_target = {"M": 1, "B": 0}
# initially, df_target contains column called diagnosis, with rows of "M" or "B" each row
df_target = replace_target(df_target, "diagnosis", map_values_target)

## TASK 5
# get the big X matrix
feature = prepare_feature(df_feature)
# get the y vector
target = prepare_target(df_target)
