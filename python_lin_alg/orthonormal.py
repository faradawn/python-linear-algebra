from numpy import *
from sympy import *

v1 = array([2,3,6])
v2 = array([3,-6,2])
x = array([49,49,49])

# converts into unit array
def unit(v):
    v = v/sqrt(sum(v**2))
    return v

u1 = unit(v1)
v2_perp = v2 - (v2.dot(u1)*(u1))
u2 = unit(v2_perp)
print("v2 perp:", v2_perp)
print("u1:", u1)
print("u2: ", u2)

# projection matrix
Q = array([u1,u2]) # transposed
proj = Q.T.dot(Q)
print("\nproj matrix: \n", proj)
print("proj result: \n", proj.dot(x))


from analyze_mat import *
A = Matrix(proj)
analyze_mat(A)