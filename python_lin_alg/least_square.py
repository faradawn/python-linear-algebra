from numpy import *
from sympy import *

# v1 and v2 for matrix A
v1 = array([5,4,2,2])
v2 = array([3,6,7,-2])
A = array([v1,v2]).T

b = array([27,0,0,0]).T


def least_sqr(A, b):
    mult = (matmul(A.T, A))
    print("inside inv: ", mult)
    mult1 = linalg.inv(mult)
    print("after inv:",mult1)
    mult2 = mult1.dot(A.T)
    print("after A^T:", mult2)
    mult3 = mult2.dot(b)
    return mult3

# x_star = least_sqr(A, b)
# error = b - A.dot(x_star)
# print("A * x_star: ", A.dot(x_star))
# error_modulus = sum(error**2)

# print("x star:", x_star)
# print("error vecor: ", error)
# print("error modulus: sqrt", error_modulus)


