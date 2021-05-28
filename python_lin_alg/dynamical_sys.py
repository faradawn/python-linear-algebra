from sympy import *
from fractions import Fraction

A = Matrix([[0.89,0,0],[0.1,0.95,0],[0.01,0.05,1]])

print(A.diagonalize())