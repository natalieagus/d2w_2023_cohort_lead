# You can define fixtures in other Python files, but they won't be automatically discovered by Pytest across multiple test files. If you define fixtures in a file other than conftest.py, you'll need to explicitly import and use those fixtures in the specific test file where they are defined.
try:
    from source.cs_0 import get_features_targets, df, replace_target, split_data, normalize_z, prepare_feature, prepare_target
except:
    print("cs_0 not implemented yet")

try: 
    from source.cs_3 import gradient_descent_logreg
except: 
    print("cs_3 not implemented yet")

try:
    from source.cs_4 import predict_logreg
except:
    print("cs_4 not implemented yet")
    
try:
    from source.cs_6 import confusion_matrix
except:
    print("cs_6 not implemented yet")
    
import pytest 
import numpy as np 

## Global variables shared between tests
def pytest_configure():
    pytest.plot_output = False 

def prepare_features_target_beta():
    try: 
        columns = ["radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean", "compactness_mean", "concavity_mean"]
        df_features, df_target = get_features_targets(df, columns, ["diagnosis"])
        df_target = replace_target(df_target, "diagnosis", {'M': 1, 'B': 0})

        df_features_train, df_features_test, df_target_train, df_target_test = split_data(df_features, df_target, random_state=100, test_size=0.3)
        df_features_train_z, _, _ = normalize_z(df_features_train)

        features = prepare_feature(df_features_train_z)
        target = prepare_target(df_target_train)

        iterations = 1500
        alpha = 0.01
        beta = np.zeros((features.shape[1],1))

        beta, _ = gradient_descent_logreg(features, target, beta, alpha, iterations)
        return df_features_test, df_target_test, beta
    except:
        return None, None, None


@pytest.fixture 
def features_target_beta():
   return prepare_features_target_beta()