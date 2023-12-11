import aocd
import re
rx = re.compile(r'[0-9]+')

data = aocd.get_data()
debug = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
#data = debug
data = data.splitlines()
seeds = [int(x.group()) for x in rx.finditer(data[0].split(":")[1])]
index = 0
organized_data = []
for row in data[2:]:
    if row == "":
        index += 1
        continue
    if not row[0].isdigit():
        organized_data.append([])
        continue
    rd = []
    for x in rx.finditer(row):
        rd.append(int(x.group()))
    organized_data[index].append(rd)

def GetNew(level, n):
    lvl = organized_data[level]
    for m in lvl:
        if m[1]<=n and n<m[1]+m[2]:
            return m[0]+(n-m[1])
    return n
def GetOld(level, n):
    lvl = organized_data[level]
    for m in lvl:
        if m[0]<=n and n<m[0]+m[2]:
            return m[1]+(n-m[0])
    return n
def IsInSeeds(n):
    for s,step in zip(seeds[::2],seeds[1::2]):
        
        if s<=n and n<s+step:
            return True
    return False
""" for level in organized_data:
    d = {}
    for m in level:
        r_output = range(m[0],m[0]+m[2])
        r_input = range(m[1], m[1]+m[2])
        for i in range(m[2]):
            d[r_input[i]] = r_output[i]
    master_dic.append(d)
    print("Done")
"""
def getLand(new):
    for i in range(len(organized_data)):
        new = GetNew(i,new)
    return new

def getSeeds(new):
    for i in range(len(organized_data)-1,-1,-1):
        new = GetOld(i,new)
    return new
def getOut(seeds):
    out = []
    for s in seeds:
        out.append(getLand(s))
    return out
#579439039
#answer1 = getOut(seeds)
m = 1000000000000000
sas = 0
for row in organized_data[-1]:
    if row[0]+row[2]<m:
        m = row[0]+row[2]
        sas = row[0]
print(sas)
print(m)
#Awful bruteforce
for i in range(0,110359150):
    if IsInSeeds(getSeeds(i)):
        print(i)
        break