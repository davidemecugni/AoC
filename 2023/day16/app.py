import aocd, sys

sys.setrecursionlimit(1000000)

data = aocd.get_data(day=16)

debug = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""

#data = debug
data = data.splitlines()
data = [[c for c in row] for row in data]


def Explore(i,j,dir, start = False):
    if energy[i][j] > 10 or (i<0 or j<0):
        return
    energy[i][j] += 1

    ni = dir[0]+i
    nj = dir[1]+j

    if start:
        ni,nj = i,j
        #print(ni,nj,dir)

    if ni >= len(data) or nj >= len(data[0]):
        return
    
    newc = data[ni][nj]

    if newc == '.':
        Explore(ni,nj,dir)
        return
    if newc == '/' or newc == '\\':
        newd = dir[::-1]
        if newc == '/':
            newd = [-1*n for n in newd]
        Explore(ni,nj,newd)
        return
    
    if (dir[1] == 0 and newc == '|') or (dir[0] == 0 and newc == '-'):
        Explore(ni,nj,dir)
    elif (dir[1] == 0 and newc == '-'):
        Explore(ni,nj,(0,1))
        Explore(ni,nj,(0,-1))
    elif (dir[0] == 0 and newc == '|'):
        Explore(ni,nj,(1,0))
        Explore(ni,nj,(-1,0))



def CountEnergy(energy):
    s = 0
    for r in energy:
        for n in r:
            if n != 0:
                #print("#", end="")
                s += 1
            else:
                pass
    return s

max2 = 0
energy = [[0 for c in row] for row in data]
Explore(0,0,(0,1), True)
print(CountEnergy(energy))

for i in range(len(data)):
    energy = [[0 for c in row] for row in data]
    #print(i,0,dir)
    Explore(i,0,(0,1),True)
    c = CountEnergy(energy)
    if c > max2:
        max2 = c
    energy = [[0 for c in row] for row in data]
    #print(i,len(data[0])-1,dir)
    Explore(i,len(data[0])-1,(0,-1),True)
    c = CountEnergy(energy)
    if c > max2:
        max2 = c
for i in range(len(data[0])):
    energy = [[0 for c in row] for row in data]
    #print(0,i,dir)
    Explore(0,i,(1,0),True)
    c = CountEnergy(energy)
    if c > max2:
        max2 = c
    energy = [[0 for c in row] for row in data]
    Explore(len(data)-1,i,(-1,0),True)
    c = CountEnergy(energy)
    if c > max2:
        max2 = c

print(max2)
#7530
    