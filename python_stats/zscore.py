import numpy as np
import itertools as it
import operator as op
from functools import reduce

import scipy.stats as sci

# calculate combination
def ncr(n, r):
    r = min(r, n-r)
    result = reduce(op.mul, range(n, n-r, -1), 1) // reduce(op.mul, range(1, r+1), 1)
    return ans

# calculates z-score(0.95) = 1.645
def zscore(n):
    ans = sci.norm.ppf(n)
    return ans

# calculates P(z < 1.645) = 0.95 
def pvalue(n):
    ans = sci.norm.cdf(n)
    return ans

z = (24-100/6)/(np.sqrt(100*5/36))
print(z)
print(pvalue(z))