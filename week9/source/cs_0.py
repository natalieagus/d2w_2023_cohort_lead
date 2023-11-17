# receive df in --> the original dataframe 
# receive two opt parameters: columns_means and columns_stds
def normalize_z(dfin, columns_means=None, columns_stds=None):
    # check if opt args are given 
    if columns_means is None:
        # take the mean per column 
        # if i have 3 cols: i take the mean of each cols separately
        columns_means = dfin.mean(axis=0)
    if columns_stds is None: 
        # columns_stds is given as opt arg because if dfin only contains 1 sample (1 row), then dfin.std(axis=0) will be 0 and dfout will be error
        columns_stds = dfin.std(axis=0)
    dfout = (dfin - columns_means) / columns_stds
    # dfout is a dataframe w the same shape as dfin
    return dfout, columns_means, columns_stds

# should return two things: df_feature and df_target
def get_features_targets(df, feature_names, target_names):
    df_feature = df[feature_names]
    df_target = df[target_names]
    return df_feature, df_target # the order matter