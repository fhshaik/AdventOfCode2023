import math
with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()
list=content.split("\n")
sum=0
for i in list:
    current=-1
    line=i.split(":")[1].split("|")
    winning=line[0].split()
    having=line[1].split()
    for i in having:
        if (i in winning):
            current+=1
    sum+=math.floor(2**current)
print(sum)