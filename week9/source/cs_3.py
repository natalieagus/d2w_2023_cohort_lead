from source.cs_0 import normalize_z
from source.cs_1 import prepare_feature, calc_linreg


# this function is typically called with NEW features
# separate from those sample features given when you are
# training them via gradient descent
# these new features are called the TEST set
def predict_linreg(df_feature, beta, means=None, stds=None):
    norm_data, _, _ = normalize_z(df_feature, means, stds)
    # X matrix is basically norm_data but with extra columns of 1s
    X = prepare_feature(norm_data)
    return calc_linreg(X, beta)
    pass
