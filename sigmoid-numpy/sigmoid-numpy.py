import numpy as np

def sigmoid(x):
    x = np.asarray(x,float)
    return 1 / ( 1 + np.exp(-x));
