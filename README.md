# Simple Scripts for Calculating Linear Algebra

## 0 - Basic Operations
- [x] Calculate Unit Vector and Magnitude
- [x] Calculate RREF

## 1 - Geometric Linear Transformations
- [x] Result of Projection (2D and 3D)
- [x] Result of Reflection (2D and 3D)
- [ ] Result of Rotation
- [ ] Result of Shearing

## 2 - Kernel and Image
- [x] Finding Kernel / Null Space
- [x] Finding Image / Column Space
- [x] Finding Dimensions
- [ ] Finding Basis

## .bash_profile
```bash
alias cs="cd ~/cs152/cs152-c-programming; code ."
alias lin="cd ~/cs152/python-linear-algebra; code ."
alias by="~/faradawn/cs152/byto-web/byto-web; code .; yarn serve"

alias ..="cd .."
alias op="open ."
alias gi="git push"
alias gl="git pull"
alias de="conda deactivate"`
```


## Old Scripts
scipy integrate
```py
from scipy.integrate import quad
from sympy import *

# original function 
def x_y_func(x,y):
    return 3/2*(x**2+y**2)

# y bound
inner_hi = 1
inner_low = 0
# x bound
outer_hi = 1
outer_low = 0

# inner dy results in x function
def x_func(x):
    hi = inner_hi
    low = inner_low
    return quad(x_y_func, hi, low, args=(x))[0]

# outer dx results in numeric
result = quad(x_func, outer_hi, outer_low)[0]
```
