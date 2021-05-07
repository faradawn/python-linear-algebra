from numpy import *
from sympy import *

v1 = array([5,4,2,2])
v2 = array([3,6,7,-2])
x = array([14,-14,0,-7])

# converts into unit array
def unit(v):
    v = v/sqrt(sum(v**2))
    return v

u1 = unit(v1)
v2_perp = v2 - (v2.dot(u1)*(u1))
u2 = unit(v2_perp)
print("v2 perp:", v2_perp)

# projection matrix
Q = array([u1,u2]).T 
proj = Q.dot(Q.T)
print("\northo basis:\n", Q)
print("proj mat:\n", proj)

from analyze_mat import *
A = Matrix(proj)
analyze_mat(A)