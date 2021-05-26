from sympy import *
from fractions import Fraction

# only input matrix A
A = Matrix([[0.89,0,0],[0.1,0.95,0],[0.01,0.05,1]])
I = eye(len(A.row(0)))
x = symbols("x")
P = (A-I*x).det()
sol = solve(P, x)
# returns eigenvalues
# print("eigenvalues:", sol)

# default eignvalues and vector function
print("eigenval with multiplicity:", A.eigenvals())
print("eigenvect with geo multiplicity:", A.eigenvects()[0][2], A.eigenvects()[1][2])

# fast way: directly use diagonolization to find eigens
print("\nquick find eigen with diagonalization:")
S,D = A.diagonalize()
print("S:", S)
print("D:", D)
print("S-1:", S**-1)

# find x(t) closed formula
print("\nquick find closed formula:")
t = symbols('t')
t=10
x_t = S*(D**t)*S**-1
x_0 = Matrix([[1000],[0],[0]])
print(x_t)
print("closed formula times initial condition:")
print(x_t * x_0)
