import aocd
data = aocd.get_data()
import math
debug = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
#data = debug
data = data.splitlines()
instruction = data[0]
options = {}
for row in data[2:]:
    options[row[:3]] = {'L': row[7:10], 'R': row[12:15]}
""" 


current = 'AAA'

step1 = 0
while current != 'ZZZ':
    for c in instruction:
        current = options[current][c]
        step1 += 1
print(step1) """
#aocd.submit(step1)



def AllEndingWithZ(currents):
    total = 0
    for val in currents:
        if val[2] == 'Z':
            total += 1
    return total == len(currents)
get_ending_a = []
for k in options.keys():
    if k[2] == 'A':
        get_ending_a.append(k)
currents = get_ending_a
print(currents)
step2 = 0

first_z = [0 for i in range(len(get_ending_a))]
def DiffThanZero(first_z):
    for z in first_z:
        if z == 0:
            return False
    return True
while not DiffThanZero(first_z):
    for c in instruction:
        new_currents = []
        for cur in currents:
            new_currents.append(options[cur][c])
        currents = new_currents
        #print(currents)
        for i,c in enumerate(currents):
            if c[2] == 'Z' and first_z[i] == 0:
                first_z[i] = step2 + 1
        step2 += 1

def GetTotal(first_z):
    lcm = 1
    for i in first_z:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm
print(f"total steps: {GetTotal(first_z)}")