import aocd
import sys
sys.setrecursionlimit(100000)
data = aocd.get_data()
debug = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
#data = debug
data = data.splitlines()
maxx = len(data)
maxy = len(data[0])
allowed = {"up":['F','7','|'],"down":['L','J','|'], 'left':['F','L','-'],'right':['7','J','-']}
allowedstart = {"down":['F','7','|','S'],"up":['L','J','|','S'], 'right':['F','L','-','S'],'left':['7','J','-','S']}

def CanGo(sx,sy,ex,ey):
    if ex<0 or ey<0:
        return False
    if ex>=maxx or ey>=maxy:
        return False
    if explored[ex][ey]:
        return False
    
    if ey-sy == 1 and sx == ex and data[ex][ey] in allowed['right'] and data[sx][sy] in allowedstart['right']:
        return True
    
    if ey-sy == -1 and sx == ex and data[ex][ey] in allowed['left'] and data[sx][sy] in allowedstart['left']:
        return True
    #right
    if ey==sy and ex-sx==1 and data[ex][ey] in allowed['down'] and data[sx][sy] in allowedstart['down']:
        return True
    #left
    if ey==sy and ex-sx==-1 and data[ex][ey] in allowed['up'] and data[sx][sy] in allowedstart['up']:
        return True
    return False
def FoundStart():
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c=='S':
                return i,j
            
r = [False for i in range(len(data[0]))]
explored = [r.copy() for i in range(len(data))]
meetNr = False

ways = 0
step = 0


def Explore(x,y):
    explored[x][y] = True
    poly.append([x,y])
    went = 0
    t = 0
    if CanGo(x,y,x+1,y):
        t += 1 +Explore(x+1,y)
    elif CanGo(x,y,x-1,y):
        t += 1+ Explore(x-1,y)
    elif CanGo(x,y,x,y+1):
        t += 1+ Explore(x,y+1)
    elif CanGo(x,y,x,y-1):
        t += 1+ Explore(x,y-1)
    return went + t 

i,j = FoundStart()
poly = []
ways = 0
if CanGo(i,j,i+1,j):
    ways+=1
if CanGo(i,j,i,j+1):
    ways+=1
if CanGo(i,j,i-1,j):
    ways+=1
if CanGo(i,j,i,j-1):
    ways+=1

returned = Explore(i,j)
#print(ways, returned)
print((returned+1)//2)
d = {False:'F', True:'T'}
""" 
for row in explored:
    for c in row:
        print(d[c], end="")
    print("") 
"""


#out true, ins false
r = [False for i in range(len(data[0]))]
insout = [r.copy() for i in range(len(data))]

allowed = {"up":['J','L'],"down":['7','F'], 'left':['7','J'],'right':['F','L']}
def CanGoOutside(sx,sy,ex,ey):
    if ex<0 or ey<0:
        return False
    if ex>=maxx or ey>=maxy:
        return False
    if explored[ex][ey]:
        return False
    if ey-sy == 1 and sx == ex and data[ex][ey] in allowed['right']:
        return True
    if ey-sy == -1 and sx == ex and data[ex][ey] in allowed['left']:
        return True
    #right
    if ey==sy and ex-sx==1 and data[ex][ey] in allowed['down']:
        return True
    #left
    if ey==sy and ex-sx==-1 and data[ex][ey] in allowed['up']:
        return True
    return False

def ExploreOutside(x,y):
    insout[x][y] = True
    went = 0
    t = 0
    if CanGoOutside(x,y,x+1,y):
        Explore(x+1,y)
    if CanGoOutside(x,y,x-1,y):
        Explore(x-1,y)
    if CanGoOutside(x,y,x,y+1):
        Explore(x,y+1)
    if CanGoOutside(x,y,x,y-1):
        Explore(x,y-1)
    #return went + t 
#print(poly)
from matplotlib.path import Path
i,j = FoundStart()
ans_2 = 0
p = Path(poly)
for x in range(len(data)):
    for y in range(len(data[0])):
        if [x, y] in poly:
            continue
        if p.contains_point((x, y)):
            ans_2 += 1
print(ans_2)