import aocd, sys
sys.setrecursionlimit(10000)

data = aocd.get_data(day=12,year=2023)
debug = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

#data = debug
data = data.splitlines()
nd = []
for row in data:
    row = row.split(" ")
    #print(row)
    row[1] = [int(x) for x in row[1].split(",")]
    nd.append(row)
data = nd

def IsOk(stri, data):
    index = 0
    started = False
    count = [0 for i in range(len(data))]
    for i,c in enumerate(stri):
        if index == len(data):
            return count == data and '#' not in stri[i:]
        if c == '#':
            count[index] = count[index] + 1
            started = True
        if c == '.':
            if started:
                index += 1
            started = False
    return count == data

def Sub(stri, data):
    total = 0
    if '?' not in stri:
        if IsOk(stri, data):
            #print(stri)
            return 1
    else:
        stri = list(stri)
        s = stri.index("?")
        stri[s] = '.'
        total += Sub("".join(stri),data)
        stri[s] = '#'
        total += Sub("".join(stri),data)
    return total
"""
l1 = []
sum1 = 0
for row in data:
    n = Sub(row[0],row[1])
    #print(n, row[0])
    l1.append(n)
    sum1 +=n
print(sum1)
"""
data = aocd.get_data(day=12,year=2023).strip()
L = data.split('\n')
G = [[c for c in row] for row in L]

DP = {}
def f(dots, blocks, i, bi, current):
  key = (i, bi, current)
  if key in DP:
    return DP[key]
  if i==len(dots):
    if bi==len(blocks) and current==0:
      return 1
    elif bi==len(blocks)-1 and blocks[bi]==current:
      return 1
    else:
      return 0
  ans = 0
  for c in ['.', '#']:
    if dots[i]==c or dots[i]=='?':
      if c=='.' and current==0:
        ans += f(dots, blocks, i+1, bi, 0)
      elif c=='.' and current>0 and bi<len(blocks) and blocks[bi]==current:
        ans += f(dots, blocks, i+1, bi+1, 0)
      elif c=='#':
        ans += f(dots, blocks, i+1, bi, current+1)
  DP[key] = ans
  return ans

for part2 in [False,True]:
  ans = 0
  for line in L:
    dots,blocks = line.split()
    if part2:
      dots = '?'.join([dots, dots, dots, dots, dots])
      blocks = ','.join([blocks, blocks, blocks, blocks, blocks])
    blocks = [int(x) for x in blocks.split(',')]
    DP.clear()
    score = f(dots, blocks, 0, 0, 0)
    ans += score
  print(ans)