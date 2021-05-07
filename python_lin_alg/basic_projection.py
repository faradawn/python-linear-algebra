import numpy as np 

# the input for functions are arrays
x = np.array([1,3])
v = np.array([1,2])
a = np.array([3,4])

# converts into unit array
def unit(w):
    mag = np.sqrt(np.sum(w*w))
    w = w/mag
    print("unit vector: \n", w)
    return w

# computes projection matrix 
def proj_mat(w):
    u = unit(w)
    T = np.array([[u[0]**2, u[0]*u[1]],[u[0]*u[1], u[1]**2]])
    print("proj matrix: \n", T)
    return T

# computes the result of projection
def proj_calc(x, w):
    u = unit(w)
    T = np.sum(x*u)*u
    T = T.reshape(2,1)
    print("proj result: \n",T)
    return T

proj_mat(v)
proj_calc(x,v)