import numpy as np
from scipy import optimize

def fn(x):
	return x**2 + 5*np.sin(x)

minValue = optimize.minimize(fn,x0=2,method='bfgs',options={'disp':True})
print(minValue)

minValueWithoutOpt = optimize.minimize(fn,x0=2,method='bfgs')
print(minValueWithoutOpt)