import math
with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()
lst=content.split("\n")
lowest=-1
lowestseed=0
seeds=lst[0].split(':')[1].split()
seeds = [int(seed) for seed in seeds]

def findNextNumber(seed, lineNum):
    i=lineNum
    while(not lst[i]==""):
        numberList=lst[i].split()
        numberList=[int(number) for number in numberList]
        
        limit1=numberList[1]<=seed
        limit2=seed<(numberList[1]+numberList[2])

        if(limit1 and limit2):

            return numberList[0]+seed-numberList[1]
        i=i+1
    return seed


print((seeds[1],3))

for seed in seeds:
    number=findNextNumber(findNextNumber(findNextNumber(findNextNumber(findNextNumber(findNextNumber(findNextNumber(seed,3),21),56),84),124),136),175)
    if(lowest==-1 or number<lowest):
        lowestseed=seed
        lowest=number

print(lowestseed,lowest)