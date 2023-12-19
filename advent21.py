import re


with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\input", 'r') as file:
    content = file.read()

list=content.split("\n")
sum=0

maxvalue={"red":0, "green": 0, "blue": 0}

for i in list:
    line=i.split(":")
    validGame=True

    maxvalue={"red":0, "green": 0, "blue": 0}
    
    for j in re.split(';|,',line[1]):
        if(maxvalue[j.split()[1]]<int(j.split()[0])):
            maxvalue[j.split()[1]]=int(j.split()[0])
    sum+=maxvalue["red"]*maxvalue["blue"]*maxvalue["green"]
    

print(sum)