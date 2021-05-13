from numpy import *
from sympy import *
import fractions
set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

# V = span(v1, v2) 
v1 = array([5,4,2,2])
v2 = array([3,6,7,-2])
A = array([v1,v2]).T

# x to be projected 
x = array([14,-14,0,-7]).T

def proj(A):
    inner = linalg.inv(A.T.dot(A))
    res = matmul(matmul(A, inner), A.T)
    return res

print("proj matrix: \n", proj(A))
print("\nproj * x:", proj(A).dot(x))
