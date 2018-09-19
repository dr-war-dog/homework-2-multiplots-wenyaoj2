import matplotlib.pyplot as plt
import datetime
import csv
import numpy as np
import pandas as pd
data = {}
f = open("Dataset/gun-violence.csv")
df = pd.DataFrame.from_csv("Dataset/gun-violence.csv")

print(type(df))
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
plt.plot(df["n_killed"])
plt.show()
num_injured = filter_gh(data, "n_injured",0)
sum1 = []
sum_injured = 0
for k in num_injured:
    sum1.append(num_injured[k])
for k in range(len(sum1)):
    sum_injured = sum_injured + sum1[k]

print("The sum of the number of injured is : ",sum_injured)
# result = filter_gh(data,)
plt.plot(df["n_injured"])
plt.show()

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
result3 = np.array(result["n_injured"])
sum = result3.sum(axis =0)
print("The sum of injuried between 1.1 to 2.1: "+str(sum))
plt.plot(result["date"],result["n_injured"],"og")
plt.show()

countcd = 0
count = 0
for index, row in df.iterrows():
    countcd = countcd + row["congressional_district"]
    if not np.isnan(row["n_guns_involved"]):
        count = count + row["congressional_district"]
print(str((count/countcd)*100)+"% percent of districts are involved ")

new_df = df.sort_values(by="n_injured", ascending = False)
print("the highest number of injuries are")
count = 0
for index, row in new_df.iterrows():
    count = count + 1
    if count<10:
        print(row["address"])
