
with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\input", 'r') as file:
    content = file.read()


valid = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }

list=content.split("\n")
sum=0
for i in list:
    presum=sum
    for j in range(len(i)):
        found=False
        for a in valid:
            if(a in i[:(j+1)]):
                sum+=10*valid[a]
                found=True
                break
        if(found):
            break
    last=0
    found=False
    for j in range(len(i)):
        for a in valid:
            if(a in i[-(j+1):]):
                sum+=valid[a]
                found=True
                break
        if(found):
            break
    print(sum-presum)

print(sum)

