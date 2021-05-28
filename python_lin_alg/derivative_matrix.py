from sympy import *

x,y,r,s,t = symbols('x,y,r,s,t')

y = 1
x = 0

r=x*y
s=exp(2*x)
t=x**3 - y**3

Df = Matrix([[y,x],[exp(2*x),0],[3*x**2, -3*y**2]])
Dg = Matrix([[s*t,r*t,r*s],[1,1,1]])

print(Dg * Df)