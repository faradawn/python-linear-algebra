# method 1: scipy
from scipy.integrate import quad

# original function 
def x_y_func(x,y):
    return x*y*(3/8)*(x+y)**2
# y bound
inner_hi = 1
inner_low = -1
# x bound
outer_hi = 1
outer_low = -1


# inner dy results in x function
def x_func(x):
    hi = inner_hi
    low = inner_low
    return quad(x_y_func, hi, low, args=(x))[0]

# outer dx results in numeric
result = quad(x_func, outer_hi, outer_low)[0]

print(result)


# method 2: sympy
from sympy import *

x, y = symbols("x y")
f = x*y*(3/8)*(x+y)**2

# inner dy first, then outer dx
res = integrate(f, (y, inner_low, inner_hi), (x, outer_low, outer_hi))

print(res)

