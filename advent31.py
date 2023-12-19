
with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()
list=content.split("\n")



def getNumber(i,j,list):
    k=0
    while(0<j-k and list[i][j-k].isdigit()):
        k=k+1
    l=0
    while(j+l<len(list[i])and list[i][j+l].isdigit()):
        l=l+1
    number=list[i][j-k+1:j+l]
    return (int(number),(i,j-k+1,j+l))



def getLineGear(i,list):
    sum=0
    j=0
    while(j<len(list[i])):
        if(list[i][j]=='*'):

            validLocations=isAdjacent(i,j,list)

            if(len(validLocations)==2):
                sum+=validLocations[0]*validLocations[1]
        j=j+1
    return sum



def isAdjacent(i,j,list):
    valid=[]
    blacklist=[]
    for k in range(9):
        limits1=(0<=(i-1)+k//3)and ((i-1)+k//3<len(list))
        limits2=((0<=(j-1)+k%3)and((j-1)+k%3<len(list[i])))
        limits3=True
        for d in blacklist:
            if(((i-1)+k//3==d[0])and (d[1]<=((j-1)+k%3) and (((j-1)+k%3)<d[2]) )):
                limits3=False
        if(limits1 and limits2 and limits3):
           
            ch=list[(i-1)+k//3][(j-1)+k%3]
            
            if (ch.isdigit()):
                tuple=getNumber((i-1)+k//3,(j-1)+k%3,list)
                valid.append(tuple[0])
                blacklist.append(tuple[1])

    if(len(valid)==2):
        print(valid)
        return valid
    return []


sum=0

for i in range(len(list)):
    sum+=getLineGear(i,list)

print(sum)