from pandas import *
import csv

# remove trailing comma: sed 's/,$//' test.csv > temp.csv
# add header: sed $'1s/^/<column names>\\\n&/‘ temp.csv > out.csv

# panda print data frame with sort
data = read_csv("./data/out.csv")
data = data.sort_values(by="cnet")
print(data)

