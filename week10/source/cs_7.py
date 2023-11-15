import numpy as np


def calc_accuracy(cm):
    negneg, pospos, negpos, posneg = cm[(0, 0)], cm[(1, 1)], cm[(0, 1)], cm[(1, 0)]

    return {
        "accuracy": (negneg + pospos) / np.sum(list(cm.values())),
        "sensitivity": pospos / (pospos + posneg),
        "specificity": negneg / (negneg + negpos),
        "precision": pospos / (pospos + negpos),
    }
