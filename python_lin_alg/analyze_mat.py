import numpy as np
from sympy import Matrix

# input the matrix
A = Matrix([[1,2,3,4],[1,2,2,4],[2,1,6,8],[1,2,3,6]])


def analyze_mat(A):
    # row reduced form
    print("\n === analyzing matrix === ")
    print("rref: \n",A.rref()[0])
    print("pivot columns: \n", A.rref()[1])

    # finding the kernel (null space)
    kernel = A.nullspace()
    print("\nkernel vectors: ", len(kernel))
    i = 0
    while i < len(kernel):
        print(kernel[i])
        i+=1

    # finding the image (column space˜
    image = A.columnspace()
    print("\nimage vectors: ", len(A.rref()[1]))
    i = 0
    while i < len(image):
        print(image[i])
        i+=1
    
    # inverse and determinant
    if A.det() == 0:
        print("\ninvertible: false")
    else:
        print("\ninvertible: true")
        print("det: ", A.det())


analyze_mat(A)
