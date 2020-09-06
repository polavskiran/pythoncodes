from scipy.integrate import quad

def integrateFunction(x):
	return x

print(quad(integrateFunction,0,1))

def integrateFn(x,a,b):
	return x*a+b

a=3
b=2
print(quad(integrateFn,0,1,args=(a,b)))