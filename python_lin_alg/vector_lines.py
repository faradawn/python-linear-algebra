from sympy import *

# two vector lines intersection point
def arr_1(t):
    return Matrix([2+t,3-2*t,1-3*t])

def arr_2(t):
    return Matrix([3+t, -4+3*t, 2-7*t])

def l1():
    r0 = arr_1(0)
    d = arr_1(1)-arr_1(0)
    print("l1: ",r0, " + t * ",d)
    return d
def l2():
    r0 = arr_2(0)
    d = arr_2(1) - arr_2(0)
    print("l2: ", r0, " + t * ",d)
    return d
def intersect():
    left = arr_1(2)-arr_2(2)
    right = l2() - l1()
    print("left: ", left)
    print("right: t *", right)

intersect()

