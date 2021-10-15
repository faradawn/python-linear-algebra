from sympy import *

# declare your variables
x, y, c = symbols("x y c")
# enter your f(x,y) here
f = 3/2*(x**2+y**2)
# enter your inner bound for dx, then dy
x_hi = 1
x_low = 0
y_hi = 1
y_low = 0

# solve for constant 
# raw = integrate(f, (x, inner_low, inner_hi), (y, outer_low, outer_hi))
# res = solve(Eq(raw, 1), c)
# print(res)

# calculate x's marginal density
fx = integrate(f, (y, y_low, y_hi))
print(fx)
