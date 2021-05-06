# method 1: scipy
from scipy.integrate import quad

# original function 
def x_y_func(x,y):
    return 24*x*y

# inner dy results in x function
def x_func(x):
    inner_hi = 1-x
    inner_low = 0
    return quad(x_y_func, inner_hi, inner_low, args=(x))[0]

# outer dx results in numeric
outer_hi = 1
outer_low = 0
result = quad(x_func, outer_hi, outer_low)[0]

print(result)


# method 2: sympy
from sympy import *

x, y = symbols("x y")
f = 24*x*y

inner_hi = 1-x
inner_low = 0
# inner dy first, then outer dx
res = integrate(f, (y, inner_low, inner_hi), (x, outer_low, outer_hi))

print(res)
