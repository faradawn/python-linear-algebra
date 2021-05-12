import numpy as np
from sympy import Matrix

# initializing a few matrices
A = Matrix([[1,1],[1,0],[0,1]])


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
        print("\ninvertible: true")
    else:
        print("\ninvertible: false")
    

analyze_mat(A)