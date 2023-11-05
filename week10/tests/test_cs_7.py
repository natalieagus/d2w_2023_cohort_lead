
import numpy as np 
try: 
    from source.cs_6 import confusion_matrix
    from source.cs_4 import predict_logreg
    from source.cs_7 import calc_accuracy
except:
    print("cs_4, cs_6, and cs_7 not implemented yet")


def test_cs_7(features_target_beta):
    df_features_test, df_target_test, beta = features_target_beta 
    pred = predict_logreg(df_features_test, beta)
    result = confusion_matrix(df_target_test.values, pred, [1,0])
    ans = calc_accuracy(result)
    expected = {'accuracy': 0.9235294117647059, 'sensitivity': 0.8260869565217391, 'specificity': 0.9900990099009901, 'precision': 0.9827586206896551}
    assert np.isclose(ans['accuracy'], expected['accuracy'])
    assert np.isclose(ans['sensitivity'], expected['sensitivity'])
    assert np.isclose(ans['specificity'], expected['specificity'])
    assert np.isclose(ans['precision'], expected['precision'])
    