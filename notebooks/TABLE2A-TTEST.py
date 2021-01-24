## Import the packages
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

##  2 random distributions
#Sample Size
N = 500

a = np.array([3.05,3.14,2.48,2.26])

b = np.array([1.19,1.21,1.65,1.03])


## Calculating the Standard Deviation and Variance for Table 2A
#


var_a = np.var(a)
var_b = np.var(b)

#std deviation
s = np.sqrt((var_a + var_b)/2)
s



## Calculate the t-statistics
t = (a.mean() - b.mean())/(s*np.sqrt(2/N))



## Compares with the critical t-value
#Degrees of freedom
df = 2*N - 2

#p-value after comparison with the t 
p = 1 - stats.t.cdf(t,df=df)


print("t = " + str(t))
print("p = " + str(2*p))
###  after comparing the t statistic with the critical t value (computed internally) we get a good p value of 0.0005 and thus we reject the null hypothesis and thus it proves that the mean of the two distributions are different and statistically significant.


## Cross Checking with the internal scipy function
t2, p2 = stats.ttest_ind(a,b)
print("t = " + str(t2))
print("p = " + str(p2))