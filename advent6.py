
with open("C:\\Users\\cosmi\\OneDrive\\Documents\\Coding\\Aoc\\input", 'r') as file:
    content = file.read()
lst=content.split("\n")

distance=lst[1].split(":")[1].split()
time=lst[0].split(":")[1].split()
time=[int(number) for number in time]
distance=[int(number) for number in distance]
print(time)
print(distance)

product=1
for a in range(len(time)):
    sum=0
    for i in range(1,time[a]):
        if((i+(distance[a]/i))<time[a]):
            sum+=1
    product=product*sum

print(product)