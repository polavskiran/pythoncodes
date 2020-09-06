import numpy as np
from scipy.optimize import root

def rootfunc(x):
	return x + 3.5 * np.cos(x)

rootValue = root(rootfunc,0.3)
print(rootValue)