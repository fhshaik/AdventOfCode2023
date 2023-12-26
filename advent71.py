with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()
lst=content.split("\n")


cardValue={"A":12, "K":11, "Q":10, "T":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1, "J":0}

cards=[]


for i in lst:
    cards.append((i.split()[0],int(i.split()[1])))


def card2hex1(string):
    sum=0
    n=len(string)
    for i in range(1,n+1):
        sum+=(13**(n-i))*cardValue[string[i-1]]
    return sum

def card2hex2(string):
    string1=string.replace("J","")
    try:
        res= max(string1, key=lambda x: string1.count(x))
    except:
        res='O'
    
    string1=string1.replace(res,"")
    
    try:
        res2= max(string1, key=lambda x: string1.count(x))
    except:
        res2='O'
    strength=2*(string.count(res)+string.count("J"))+string.count(res2)-1
    return ((13**6)*strength)+card2hex1(string)

def card2hex3(tuple):
    return card2hex2(tuple[0])


cards.sort(key=card2hex3)

sum=0
for i in range(len(cards)):
    sum+=cards[i][1]*(i+1)

print(sum)