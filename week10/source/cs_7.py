import numpy as np 

def calc_accuracy(cm):
    ### BEGIN SOLUTION
    negneg = cm[(0,0)]
    pospos = cm[(1,1)]
    negpos = cm[(0,1)]
    posneg = cm[(1,0)]
    accuracy = (negneg + pospos) / np.sum(list(cm.values()))
    sensitivity = pospos / (pospos + posneg)
    specificity = negneg / (negneg + negpos)
    precision = pospos / (pospos + negpos)
    ### END SOLUTION
    result = {'accuracy': accuracy, 'sensitivity': sensitivity,
              'specificity': specificity, 'precision': precision}
    return result
