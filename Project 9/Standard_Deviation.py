import csv
import math

with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

print(file_data[0])
data=file_data[0]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)

    mean = total/n
    return mean

#squsquaring and getting values
squared_list =[]
for number in data:
    a=int(number) - mean(data)
    a=a**2
    squared_list.append(a)

#getting the sum
sum=0
for y in squared_list:
    sum+=y

#dividing the sum by total values
result = sum / (len(data)-1)

#taking the squareroot to get standard deviation
standard_deviation = math.sqrt(result)

print(standard_deviation)