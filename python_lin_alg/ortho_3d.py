from numpy import *
from sympy import *

v1 = array([2,2,1])
v2 = array([-2,1,2])
v3 = array([18,0,0])

x = array([49,49,49])

# converts into unit array
def unit(v):
    v = v/sqrt(sum(v**2))
    return v

u1 = unit(v1)
v2_perp = v2 - (v2.dot(u1)*(u1))
u2 = unit(v2_perp)

v3_perp = v3 - v3.dot(u1)*u1 - v3.dot(u2)*u2
u3 = unit(v3_perp)

print("v2 perp:", v2_perp)
print("u3 perp:", v3_perp)

# projection matrix
Q = array([u1,u2,u3]).T # transposed
proj = Q.dot(Q)
print("\northo basis:\n", Q)
print("\nproj matrix:\n", proj)


from numpy.linalg import inv

M = array([[2,-2,18],[2,1,0],[1,2,0]])
R = array([[3,0,12],[0,3,-12],[0,0,6]])
print("\nQ * R = M is owrking:\n",matmul(Q,R))
print("why inv(Q) * M == R is not?")


from analyze_mat import *
A = Matrix(proj)
# analyze_mat(A)