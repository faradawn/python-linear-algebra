from numpy import *
from sympy import *

A = array([[5,3],[4,6],[2,7],[2,-2]])
b = array([27,0,0,0]).T
x = array([14,-14,0,-7]).T

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


def proj(A):
    inner = linalg.inv(matmul(A.T, A))
    front = matmul(A, inner)
    res = matmul(front, A.T)
    return res

print("proj matrix: ", proj(A))
print("proj * x:", proj(A).dot(x))
