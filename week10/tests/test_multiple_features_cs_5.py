import numpy as np

try:
    from source.cs_0 import (
        get_features_targets,
        df,
        replace_target,
        split_data,
        normalize_z,
        prepare_feature,
        prepare_target,
    )
    from source.cs_3 import gradient_descent_logreg
    from source.cs_4 import predict_logreg
except:
    print("cs_0, cs_3, and cs_4 not implemented yet")
import matplotlib.pyplot as plt
import pytest


def test_cs_5():
    columns = [
        "radius_mean",
        "texture_mean",
        "perimeter_mean",
        "area_mean",
        "smoothness_mean",
        "compactness_mean",
        "concavity_mean",
    ]

    # extract the features that we are concerned with, and give the name of the target column
    df_features, df_target = get_features_targets(df, columns, ["diagnosis"])
    # to replace the target column with integer instead of "M" or "B" because we can't run grad-desc with characters (strings)
    df_target = replace_target(df_target, "diagnosis", {"M": 1, "B": 0})

    # split the dataset
    df_features_train, df_features_test, df_target_train, df_target_test = split_data(
        df_features, df_target, random_state=100, test_size=0.3
    )
    # normalise so that we dont run into floating point error
    df_features_train_z, means, stds = normalize_z(df_features_train)

    # prepare the X matrix and the y target arrays / vector
    features = prepare_feature(df_features_train_z)
    target = prepare_target(df_target_train)

    iterations = 1500
    alpha = 0.01
    beta = np.zeros((features.shape[1], 1))

    # train with gradient descent
    beta, J_storage = gradient_descent_logreg(features, target, beta, alpha, iterations)

    assert beta.shape == (8, 1)
    ans = np.array(
        [
            [-0.6139379],
            [0.82529554],
            [0.72746485],
            [0.8236603],
            [0.81647937],
            [0.5057749],
            [0.44176466],
            [0.78736842],
        ]
    )
    assert np.isclose(beta, ans).all()

    # call predict() on one record to get the predicted values
    # use the variable 'means' and 'stds' to normalize
    input_1row = np.array([[12.22, 20.04, 79.47, 453.1, 0.10960, 0.11520, 0.08175]])

    # predict with now trained beta, just plug into the p(x) equation
    pred_1row = predict_logreg(input_1row, beta, means, stds)
    assert pred_1row[0][0] == 0

    if pytest.plot_output:
        plt.plot(J_storage)
        plt.show()

    pred = predict_logreg(df_features_test, beta)

    if pytest.plot_output:
        plt.figure(1)
        plt.scatter(df_features_test["radius_mean"], df_target_test)
        plt.scatter(df_features_test["radius_mean"], pred)
        plt.title("radius_mean")
        plt.figure(2)
        plt.scatter(df_features_test["texture_mean"], df_target_test)
        plt.scatter(df_features_test["texture_mean"], pred)
        plt.title("texture_mean")
        plt.figure(3)
        plt.scatter(df_features_test["perimeter_mean"], df_target_test)
        plt.scatter(df_features_test["perimeter_mean"], pred)
        plt.title("perimeter_mean")
        plt.show()
