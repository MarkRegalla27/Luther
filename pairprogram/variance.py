import math
import numpy as np

List1 = [2,3,8,5,6]
List2 = [5,8,3,4,6]
#List3 = [4,9,7,1,2]

mean1 = np.mean(List1)
mean2 = np.mean(List2)

sum1 = 0
sum2 = 0
for i in List1:
    sum1 = sum1 + (i - mean1)**2

var1 = sum1 / len(List1)
print 'Manually calculated variance: ' + str(var1)

var2 = np.var(List1)
print 'Numpy variance: ' + str(var2)

for i, n in enumerate(List1):
    sum2 = sum2 + (List1[i] - mean1)*(List2[i] - mean2)

covar1 = sum2 / (len(List1) - 1)
print 'Manually calculated covariance: ' + str(covar1)

covar2 = np.cov(List1, List2)
print 'Numpy Covariance: ' + str(covar2)