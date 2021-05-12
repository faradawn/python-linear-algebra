from numpy import *
from sympy import *

A = array([[1,1],[1,0],[0,1]])
b = array([3,3,3])
mult = matmul(A.T, A)

res = mult.dot(A.T).dot(b.T)

print(b-A.dot(res))

