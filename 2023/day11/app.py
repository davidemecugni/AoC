import aocd
import itertools

data = aocd.get_data()
debug = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
#data = debug
data = data.splitlines()
def IsStretch(n, type):
    if type == 'row':
        if all(x == '.' for x in data[n]):
            return True
        return False
    if type == 'col':
        for i, row in enumerate(data):
            if row[n] != '.':
                return False
        return True
newrow = []
newcol = []
def updateData():
    for i, row in enumerate(data):
        if IsStretch(i, 'row'):
            newrow.append(i)
    for i in range(len(data[0])):
        if IsStretch(i,'col'):
            newcol.append(i)
updateData()
Numbers = []
def FindNumbers():
    counter = 0
    for i,row in enumerate(data):
        for j,c in enumerate(row):
            if c == '#':
                Numbers.append((i,j))
                counter += 1
    return counter
total = FindNumbers()
#print(Numbers)
print(newcol)
print(newrow)
comb = [x for x in itertools.combinations(Numbers,2)]
totaldst = 0

def Stretch(a,b, type, coef):
    to_work = []
    if type == 'row':   
        to_work = newrow
    else:
        to_work = newcol
    if b > a:
        a, b = b, a
    total_s = 0
    for i in range(b,a):
        if i in to_work:
            total_s += 1
    return total_s * coef
for c in comb:
    dst = 0
    g1, g2 = c
    dst += abs(g1[0]-g2[0])+Stretch(g1[0],g2[0],'row',999999)
    dst += abs(g1[1]-g2[1])+Stretch(g1[1],g2[1],'col',999999)
    totaldst+= dst
print(totaldst)
aocd.submit(totaldst)
