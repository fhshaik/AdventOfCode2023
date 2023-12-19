import math
import numpy
import os
with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()
lst=content.split("\n")

array=[]
for i in range(len(lst)):
    subarray=[0]*(len(lst)+1)
    current=0
    line=lst[i].split(":")[1].split("|")
    winning=line[0].split()
    having=line[1].split()
    for j in having:
        if (j in winning):
            current+=1
    
    subarray[-1]=1
    k=0
    while(k<current and i+k<len(lst)):
        subarray[i+k+1]=1
        k=k+1
    array.append(subarray)


array.append(subarray)

matrix=numpy.transpose(numpy.array(array))

vector = numpy.array([1] * 197)
vector[-1] = 0

print((numpy.linalg.matrix_power(matrix, 10000)@vector)[-1])