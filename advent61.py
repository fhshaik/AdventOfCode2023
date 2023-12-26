with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()
lst=content.split("\n")

distance=int("".join(lst[1].split(":")[1].split()))
time=int("".join(lst[0].split(":")[1].split()))


print(time)
print(distance)



sum=0
for i in range(1,time):
    if((i+(distance/i))<time):
            sum+=1


print(sum)