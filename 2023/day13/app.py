import aocd
data = aocd.get_data(day=13, year=2023)
debug = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
#data = debug
data = data.splitlines()

newd = []
m = []
for row in data:
    if row == "":
        newd.append(m)
        m=[]
        continue
    else:
        m.append(row)
newd.append(m)
data = newd
def CheckMatching(i,i2,m):
    while (i>=0 and i2<len(m)):
        if not m[i]==m[i2]:
            return False
        i -= 1
        i2 += 1
    return True

sum1 = 0
for m in data:
    #print(m)
    symmx = 0
    for i in range(len(m)-1):
        if  CheckMatching(i,i+1,m):
            symmx = i, i+1
    symmy = 0
    m = list(zip(*m[::-1]))
    for i in range(len(m)-1):
        if  CheckMatching(i,i+1,m):
            symmy = i, i+1
    if symmy != 0:
        sum1 +=  (symmy[0]+1)
    elif symmx != 0:
        sum1 += (symmx[0]+1)*100

def CheckMatchingNotIncluded(i,i2,m):
    i = i-1
    i2 = i2 + 1
    while (i>=0 and i2<len(m)):
        if not m[i]==m[i2]:
            return False
        i -= 1
        i2 += 1
    return True

def rowdiff(m,i1,i2):
    d = 0
    for i in range(len(m[i1])):
        if m[i1][i] != m[i2][i]:
            d+= 1
    return d

def finddiff(m,i1,i2):
    for i in range(len(m[i1])):
        if m[i1][i] != m[i2][i]:
            return i
        
def CheckMatchingOneDiff(i,i2,m):
    totdiff = 0
    while (i>=0 and i2<len(m)):
        totdiff += rowdiff(m,i,i2)
        i -= 1
        i2 += 1
    return totdiff == 1

def OneDiff(m):
    sw = {"#": ".", ".":"#"}
    mc = m.copy()
    for i in range(len(m)-1):
        if rowdiff(mc,i,i+1) == 1 and CheckMatchingNotIncluded(i,i+1,m):
            return (i,i+1)
        if m[i] == m[i+1] and CheckMatchingOneDiff(i,i+1,m):
            return (i,i+1)


print(sum1)
sum2 = 0
for m in data:

    symmx = OneDiff(m)
    m = list(zip(*m[::-1]))
    symmy = OneDiff(m)
    if symmy != None:
        sum2 +=  (symmy[0]+1)
    elif symmx != None:
        sum2 += (symmx[0]+1)*100

print(sum2)
#not 64311