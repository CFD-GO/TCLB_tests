
import numpy as np

def test(*args):

    extra = args[0]
    f0 = np.asarray(args[extra+0])

    np.savetxt('output/stats.csv', np.array([np.min(f0), np.max(f0)]).T, delimiter=",")

    return 0
