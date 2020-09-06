#Scipy sub package - statistics
#CDF or Cumulative Distribution Function provides the cumulative probability associated with a function
#PDF or Probability Distrubution function of a continuos random variable is derivative of its CDF
from scipy.stats import norm
rvsarray = norm.rvs(loc=0,scale=1,size=10)
print('Random Variates of type: {}'.format(rvsarray))

cdfvalue = norm.cdf(5,loc=1,scale=2)
pdfvalue = norm.pdf(9,loc=0,scale=1)

print('CDF,PDF are {} , {}'.format(cdfvalue,pdfvalue))