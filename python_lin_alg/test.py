from numpy import *
from sympy import *
from analyze_mat import *

T = Matrix([[0,1,2],[0,0,2],[0,0,0]])
S = Matrix([[0,0,1],[0,1,0],[1,0,0]])
res = S*T*S**-1


A = Matrix([[8,-3],[6,-1]])
B = Matrix([[2,3],[0,5]])

analyze_mat(A)

analyze_mat(B)

