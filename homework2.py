import matplotlib.pyplot as plt
import datetime
import csv
import numpy as np
data = {}
f = open("Dataset/gun-violence.csv")
csv_reader = csv.reader(f)
header = next(csv_reader)
for k in header:
    data[k] = []
for row in csv_reader:

    for k, v in zip(header, row):

        data[k].append(v)
value_type = {"n_killed":"int","n_injured":"int", "congression":"int"}
for k in data:

    data[k] = np.array(data[k], dtype=value_type.get(k,"str"))

def filter_gh(inp, column,value):
    output ={}
    for i in range(len(inp[column])):
        if inp[column][i]>value:
            output[i]= inp[column][i]

    return output
num_killed = filter_gh(data, "n_killed",0)
sum = []
sum_killed = 0
for k in num_killed:
    sum.append(num_killed[k])
for k in range(len(sum)):
    sum_killed = sum_killed + sum[k]

print("The sum of the number of killed is : ",sum_killed)

num_injured = filter_gh(data, "n_injured",0)
sum1 = []
sum_injured = 0
for k in num_injured:
    sum1.append(num_injured[k])
for k in range(len(sum1)):
    sum_injured = sum_injured + sum1[k]

print("The sum of the number of injured is : ",sum_injured)
# result = filter_gh(data,)


def filter_equals(inp, column, value):
    output = {}
    good = []
    for i in range(len(inp[column])):

        if inp[column][i] == value:
            good.append(i)

    for k in inp:
        output[k] = inp[k][good]
    return output

def filter_compare(inp, column, value):
    output = {}
    good = []
    for i in range(0,len(inp[column])):

        if inp[column][i] > value:
            good.append(i)
    for k in inp:
        output[k] = inp[k][good]

    return output
def filter_data(inp, column, value):
    output = {}
    good = []
    for i in range(0,len(inp[column])):

        if inp[column][i] < value:
            good.append(i)
    for k in inp:
        output[k] = inp[k][good]

    return output
result = filter_compare(filter_data(data,"date","2013/2/1"),"n_injured",0)
result1 = filter_compare(data,"n_injured",0)
result2 = np.array(result1)
print(result2[0,1])
plt.plot(result["date"],result["n_injured"],"og")

