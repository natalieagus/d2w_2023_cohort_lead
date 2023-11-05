def normalize_z(dfin, columns_means=None, columns_stds=None):
    ###BEGIN SOLUTION
    if columns_means == None:
        columns_means = dfin.mean(axis=0)
    if columns_stds == None:
        columns_stds = dfin.std(axis=0)
    dfout = (dfin - columns_means) / columns_stds
    ###END SOLUTION 
    return dfout, columns_means, columns_stds

def get_features_targets(df, feature_names, target_names):
    ### BEGIN SOLUTION
    df_feature = df[feature_names]
    df_target = df[target_names]
    ### END SOLUTION
    pass
    return df_feature, df_target