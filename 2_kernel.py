import numpy as np
from sympy import Matrix

# initializing a few matrices
A = Matrix([[1,3,3,2,6],[1,3,4,2,7],[2,6,7,4,13]])
B = Matrix([[2,3],[5,8]])

# row reduced form
print("row reduced: \n",A.rref())

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

# calculating the matrix inverse and determinant
print("\ninverse matrix: \n", B**-1)
print("matrix determinant: \n", B.det())
