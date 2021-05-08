from numpy import *

# data table of pmf 
data = array([[25,32.5,40,45,52.5,65],[0.04,0.2,0.25,0.12,0.3,0.09]])

# mean and variance
mu = data[0][:].dot(data[1][:])
var = ((data[0][:]-mu)**2).dot(data[1][:])
print("mean: ", mu)
print("variance: ", var)

print((data[0][:]**2).dot(data[1][:]) - mu**2)
