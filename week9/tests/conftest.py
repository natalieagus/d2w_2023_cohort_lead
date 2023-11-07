# You can define fixtures in other Python files, but they won't be automatically discovered by Pytest across multiple test files. If you define fixtures in a file other than conftest.py, you'll need to explicitly import and use those fixtures in the specific test file where they are defined.

import pytest 
import numpy as np 
import pandas as pd 
from source.cs_0 import get_features_targets, normalize_z
from source.cs_1 import prepare_feature, prepare_target
from source.cs_4 import split_data
from source.cs_2 import gradient_descent_linreg
from source.cs_3 import predict_linreg
import os

## Global variables shared between tests
def pytest_configure():
    pytest.plot_output = False 
    
def prepare_df():
    # Get the current working directory
    current_directory = os.getcwd()

    # Check if the "week9" directory is one level above the current directory
    if os.path.basename(current_directory) == "Week 9":
        # If the script is in the "week9" directory
        file_path = os.path.join(current_directory, "data",  "housing_processed.csv")
    else:
        # If the script is one level above the "week9" directory
        file_path = os.path.join(current_directory, "week9", "data", "housing_processed.csv")

    # df = pd.read_csv("./data/housing_processed.csv")
    df = pd.read_csv(file_path)
    return df 

def get_feature_target():
    df = prepare_df() 
    df_feature, df_target = get_features_targets(df,["RM"],["MEDV"])
    return df_feature, df_target 

def normalise_features_target():
    df_feature, df_target = get_feature_target()
    df_feature_z,_,_ = normalize_z(df_feature)
    return df_feature_z, df_target

def prepare_feature_z_target():
    df_feature_z, df_target = normalise_features_target() 
    X = prepare_feature(df_feature_z)
    target = prepare_target(df_target)
    return X, target 

def prepare_target_pred():
    df = prepare_df()
    df_feature, df_target = get_features_targets(df, ["RM"], ["MEDV"])
    df_feature_train, df_feature_test, df_target_train, df_target_test = split_data(df_feature, df_target, random_state=100, test_size=0.3)
    df_feature_train_z,_,_ = normalize_z(df_feature_train)
    X = prepare_feature(df_feature_train_z)
    target = prepare_target(df_target_train)

    iterations = 1500
    alpha = 0.01
    beta = np.zeros((2,1))
    beta, _ = gradient_descent_linreg(X, target, beta, alpha, iterations)
    pred = predict_linreg(df_feature_test, beta)
    target = prepare_target(df_target_test)
    return target, pred 

@pytest.fixture 
def df_data_object():
   return prepare_df()

@pytest.fixture
def df_feature_df_target(): 
    return get_feature_target()

@pytest.fixture 
def df_feature_z_df_target():
    return normalise_features_target()

@pytest.fixture 
def x_z_target():
    return prepare_feature_z_target()

@pytest.fixture 
def target_pred():
    return prepare_target_pred()
