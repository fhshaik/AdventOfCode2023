#this does not work use advent52

import math
with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()

lst=content.split("\n")
lowest=-1
lowestseed=0
seeds=lst[0].split(':')[1].split()
seeds = [int(seed) for seed in seeds]
originalSeedRange=[]
j=0
while(j<len(seeds)-1):
    originalSeedRange.append((seeds[j],seeds[j+1]))
    j=j+2



def getRange(seed, lineNum):
    seedRange=[]
    seedRange.append(int(seed[0]))
    seedRange.append(int(seed[0])+int(seed[1]))
    trueSeed=int(seed[0])
    trueRange=int(seed[1])
    i=lineNum
    while(not lst[i]==""):
        numberList=lst[i].split()
        numberList=[int(number) for number in numberList]
        if(trueSeed<numberList[1] and numberList[1]<trueSeed+trueRange):
            seedRange.append(numberList[1])
            if(trueSeed<(numberList[1]+numberList[2]) and (numberList[1]+numberList[2])<trueSeed+trueRange):
                seedRange.append(numberList[1]+numberList[2])
            seedRange.sort()
        i=i+1
    transformedRange=[]
    j=0
    while(j<len(seedRange)-1):
        transSeed=findNextNumber(seedRange[j],lineNum)
        transRange=seedRange[j+1]-seedRange[j]
        transformedRange.append((transSeed,trueRange))
        j=j+1
        
    return transformedRange

def getNextRanges(seeds, lineNum):
    transSeedRange=[]
    for i in seeds:
        transSeedRange.extend(getRange(i,lineNum))
    return transSeedRange

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


print(getNextRanges(originalSeedRange,3))
print(getNextRanges(getNextRanges((originalSeedRange),3),21))

totalRange=getNextRanges(getNextRanges(getNextRanges(getNextRanges(getNextRanges(getNextRanges(getNextRanges((originalSeedRange),3),21),56),84),124),136),175)

min=-1
for i in totalRange:
    if (min==-1) or (i[0]<min):
        print(i)
        min=i[0]

print(min)

