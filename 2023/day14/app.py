import aocd
import numpy as np
data = aocd.get_data(day=14,year=2023)
debug =  """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

#data = debug
data = data.strip().splitlines()
data = [[c for c in row] for row in data]
G = data
sum1 = 0
def BringLeft(i,j, lastOcc):
    if data[i][j] == 'O':
        lastOcc[i] += 1
        data[i][j] = '.'
        data[i][lastOcc[i]-1] = 'O'
        return len(data[0])-lastOcc[i] + 1
    if data[i][j] == '#':
        lastOcc[i] = j + 1
    return 0

#print(data)
def rotate(G):
  R = len(G)
  C = len(G[0])
  NG = [['?' for _ in range(R)] for _ in range(C)]
  for r in range(R):
    for c in range(C):
      NG[c][R-1-r] = G[r][c]
  return NG

def roll(G):
  R = len(G)
  C = len(G[0])
  for c in range(C):
    for _ in range(R):
      for r in range(R):
        if G[r][c]=='O' and r>0 and G[r-1][c]=='.':
          G[r][c]='.'
          G[r-1][c] = 'O'
  return G

def score(G):
  ans = 0
  R = len(G)
  C = len(G[0])
  for r in range(R):
    for c in range(C):
      if G[r][c]=='O':
        ans += len(G)-r
  return ans
target = 10**9
t = 0
BY_GRID = {}
while t<target:
  t += 1
  for j in range(4):
    G = roll(G)
    if t==1 and j==0:
      print(score(G)) # part1
    G = rotate(G)
  #print('='*80)
  #show(G)
  #print('='*80)
  Gh = tuple(tuple(row) for row in G)
  if Gh in BY_GRID:
    cycle_length = t-BY_GRID[Gh]
    amt = (target-t)//cycle_length
    t += amt * cycle_length
  BY_GRID[Gh] = t

print(score(G))
