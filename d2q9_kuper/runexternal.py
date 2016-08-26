
import numpy as np

def test(*args):

    f0 = np.asarray(args[2])

    np.savetxt('output/drop_sumF.csv', np.array([np.sum(f0,axis=1),np.average(f0,axis=1)]))
