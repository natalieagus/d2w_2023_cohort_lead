import numpy as np
from source.cs_2 import calc_logreg
from source.cs_0 import normalize_z, prepare_feature


def predict_norm(X, beta):
    """
    Predict binary outcomes based on logistic regression probabilities.

    Parameters:
    - X (numpy.ndarray): Matrix of size # samples * # parameters.
    - beta (numpy.ndarray): Column vector of size # parameters representing the coefficients.

    Returns:
    numpy.ndarray: Column vector with values clamped to 0 or 1 based on logistic regression probabilities.

    Notes:
    - This function calculates the hypothesis or probability using calc_logreg().
    - The probabilities are categorized into either 0 or 1 based on a threshold of 0.5.
    - The output is a column vector with values clamped into 0 or 1.
    """
    # p is a vector containing values between 0 to 1, representing for each sample,
    # the probability of the occurrence of the diagnosis or some event being computed
    p = calc_logreg(X, beta)
    # Convert each element in p into value 0 or 1, depending on whether pi is < or > 0.5
    # Also returns a column vector, but now with values clamped into 0 or 1
    return np.where(p >= 0.5, 1, 0)


def predict_logreg(df_feature, beta, means=None, stds=None):
    """
    Predict binary outcomes using logistic regression.

    Parameters:
    - df_feature (pandas.DataFrame): Input feature data.
    - beta (numpy.ndarray): Column vector of size # parameters representing the coefficients.
    - means (numpy.ndarray, optional): Mean values for normalization. Default is None.
    - stds (numpy.ndarray, optional): Standard deviation values for normalization. Default is None.

    Returns:
    numpy.ndarray: Column vector of 1s or 0s to classify the input features.

    Notes:
    - Normalizes the features to prevent floating-point errors.
    - Computes the big X matrix by appending columns of 1 to the feature matrix.
    - Uses the predict_norm function to obtain binary predictions based on logistic regression probabilities.
    """
    # Normalize the features first to prevent floating-point errors
    norm_data, _, _ = normalize_z(df_feature, means, stds)
    # Compute the big X matrix, which appends the columns of 1 to the feature matrix
    X = prepare_feature(norm_data)
    return predict_norm(X, beta)
