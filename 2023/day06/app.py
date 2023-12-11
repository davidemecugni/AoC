import aocd
import re

def Outcomes(time,distance):
    s = 0
    for i in range(time+1):
        d = i*(time-i)
        if d>distance:
            s+= 1
    return s
rx = re.compile(r'[0-9]+')
data = aocd.get_data()
debug = """Time:        46857582
Distance:   208141212571410"""
#data = debug
data = data.splitlines()
data  = [x.split(":")[1] for x in data]
d = []
for row in data:
    d.append([int(x.group()) for x in rx.finditer(row)])

p = 1
for i in range(len(d[0])):
    time = d[0][i]
    distance = d[1][i]
    print(time,distance)
    p *= Outcomes(time,distance)
ans1 = p
#1108800
print(ans1)
#aocd.submit(ans1)
newd = []
for row in d:
    s = ""
    for num in row:
        s+=str(num)
    s = int(s)   
    newd.append(s)
ans2 = Outcomes(newd[0],newd[1])
#36919753
print(ans2)
aocd.submit(ans2)