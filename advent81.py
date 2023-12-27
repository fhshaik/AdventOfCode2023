import re
import math
from functools import reduce
with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()
lst=content.split("\n")


instructions=lst[0].split()[0]
print(instructions)
#get AAA
headIndex=0
def find(string):
    for i in range(2,len(lst)):
        if (lst[i].split("=")[0].replace(" ","")==string):
            return i

def find2(string):
    for i in range(2,len(lst)):
        if (lst[i].split("=")[0].replace(" ","")==string):
            temp=re.split(r'[ ,()]',lst[i].split("=")[1])
            return (temp[2],temp[4])

print(find2("AAA"))

def indexFind(string):
    if(string=="L"):
        return 0
    else:
        return 1

def findCycleLength(string):
    strPoint=string
    i=0
    while(strPoint[-1]!="Z"):
        strPoint=find2(strPoint)[indexFind(instructions[i%len(instructions)])]
        i+=1
    return i

lcmList=[]
for i in range(2,len(lst)):
    temp=lst[i].split("=")[0].replace(" ","")
    if temp[-1]=="A":
        lcmList.append(findCycleLength(temp))
lcm_result = reduce(lambda x, y: math.lcm(x, y), lcmList)
print(lcm_result)
