
import re


with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\input", 'r') as file:
    content = file.read()

list=content.split("\n")
sum=0

maxvalue={"red":12, "green": 13, "blue": 14}

for i in list:
    line=i.split(":")

    validGame=True
    
    for j in re.split(';|,',line[1]):
        if(maxvalue[j.split()[1]]<int(j.split()[0])):
            validGame=False
    
    if(validGame):
        sum+=int(line[0].split()[1])


print(sum)