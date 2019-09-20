
import numpy as np
from CallPythonHelper import *

def test(*args):
    cph = CallPythonHelper(*args)

    Fx = cph.getScalar(0)
    Fy = cph.getScalar(1)

    shape = Fx.shape

    X = np.zeros_like(Fx)
    Y = np.zeros_like(Fy)

    for x in range(shape[0]):
        X[:,x] = x

    for y in range(shape[1]):
        Y[y,:] = y

    L = float(np.max(X))
    X = X / L - 0.5
    Y = Y / L
    Y = Y - 0.5 * np.max(Y)

    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y,X)
    c1 = 60
    c2 = 0.0001

    Fy[:,:] = np.cos(Theta) * np.exp(-c1*R**2) * c2

    Fx[:,:] = -np.sin(Theta) * np.exp(-c1*R**2) * c2

    return 0
if __name__ == "__main__":
    test(0,np.zeros([20,10,1]),np.zeros([20,10,1]))
