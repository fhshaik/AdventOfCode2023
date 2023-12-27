import re
with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()
lst=content.split("\n")



print(lst[0])
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

strPoint="AAA"
i=0
while(strPoint!="ZZZ"):

    strPoint=find2(strPoint)[indexFind(instructions[i%len(instructions)])]
    print(strPoint)
    i+=1

print(i)