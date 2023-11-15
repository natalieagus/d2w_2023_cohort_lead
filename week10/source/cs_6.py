import itertools


def confusion_matrix(ytrue, ypred, labels):
    # initialise the output dictionary
    # confusion_matrix = (
    #     {}
    # )  # e.g: if labels is [0,1], produce a combination of these labels
    # # autogenerate the tuple of keys
    # keys = itertools.product(labels, repeat=2)

    # for j in keys:
    #     confusion_matrix[j] = 0

    # one-liner to show you're sigma
    confusion_matrix = {key: 0 for key in itertools.product(labels, repeat=2)}

    # loop through each sample, find out the value of ytrue and ypred for that sample, and add it to the count inside the confusion matrix output
    for idx in range(ytrue.shape[0]):
        confusion_matrix[(ytrue[idx, 0], ypred[idx, 0])] += 1
    return confusion_matrix
