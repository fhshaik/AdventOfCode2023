
with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()
list=content.split("\n")


def getLineSum(i,list):
    sum=0
    j=0
    while(j<len(list[i])):
        valid=False
        if (list[i][j].isdigit()):
            k=0
            while(j+k<len(list[i]) and list[i][j+k].isdigit()):
                if(isAdjacent(i,j+k,list)):
                    valid=True
                k=k+1
        if(valid):
            print(list[i][j:j+k])
            sum+=int(list[i][j:j+k])
            j=j+k-1
        j=j+1
    return sum

def isAdjacent(i,j,list):
    for k in range(9):
        if(((0<(i-1)+k//3)and ((i-1)+k//3<len(list))) and ((0<(j-1)+k%3)and((j-1)+k%3<len(list[i])))):
            ch=list[(i-1)+k//3][(j-1)+k%3]
            if (ch!='.' and (not ch.isdigit())):
                return True
    return False


sum=0

for i in range(len(list)):
    sum+=getLineSum(i,list)


print(sum)