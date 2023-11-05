from source.cs_6 import confusion_matrix
from source.cs_4 import predict_logreg

def test_cs_6(features_target_beta):
    df_features_test, df_target_test, beta = features_target_beta 
    pred = predict_logreg(df_features_test, beta)
    result = confusion_matrix(df_target_test.values, pred, [1,0])
    assert result == {(0, 0): 100, (0, 1): 1, (1, 0): 12, (1, 1): 57}