import itertools

def confusion_matrix(ytrue, ypred, labels):
    output = {}
    ### BEGIN SOLUTION
    keys = itertools.product(labels, repeat=2)

    for k in keys:
        output[k] = 0
        
    for idx in range(ytrue.shape[0]):
        output[(ytrue[idx,0], ypred[idx,0])] +=1
    ### END SOLUTION
    return output
