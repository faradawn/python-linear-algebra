from math import *

l = 2
t = 0.1
b = 3

f1 = exp(-l*b)
f2 = 1/(l*b)
f3 = l/((l-t)*exp(t*b))

print(f1, f2, f3)