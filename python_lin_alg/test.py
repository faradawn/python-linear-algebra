from sympy import *

k = symbols("k")

A = Matrix([[7,k,1,5],[1,0,k,-1],[3,0,0,2],[1,0,1,1]])
B = Matrix([[1,2,3,4],[1,2,2,4],[2,1,6,8],[1,2,3,6]])
print(A.det())

