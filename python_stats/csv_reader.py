import csv

# data = csv.reader(open("contact-info.csv"), delimiter="	")

data = open("data_sheets/test.csv")
read = csv.reader(data, delimiter=";")

print(read)
after_sort = sorted(data, key=lambda row : row[1], reverse=True)

print(after_sort)