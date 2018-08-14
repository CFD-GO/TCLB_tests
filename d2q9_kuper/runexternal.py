
import numpy as np

def test(*args):

    f0 = np.asarray(args[2])

    np.savetxt('output/stats.csv', np.array([np.min(f0), np.max(f0)]).T, delimiter=",")

    return 0
