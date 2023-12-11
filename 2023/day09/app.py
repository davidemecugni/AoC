import aocd
data = aocd.get_data()
debug = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
#data = debug
data = data.splitlines()
data = [row.split(" ") for row in data]
histories = []
def GetDiff(series):
    l = []
    for a,b in zip(series,series[1::]):
        l.append(int(b)-int(a))
    return l

def AllZeros(series):
    for s in series:
        if s != 0:
            return False
    return True
sum1 = 0
sum2 = 0
for row in data:
    row = [int(r) for r in row]
    last = row[-1]
    first = row[0]
    add = []
    sub = []
    while(not AllZeros(row)):
        row = GetDiff(row) 
        add.append(row[-1])
        sub.append(row[0])
        #print(row)
    sum1 += (sum(add)+last)
    sub = sub[::-1]
    parsum2 = 0
    for n in sub[1:]:
        parsum2 = -parsum2+n
        
    parsum2 = first - parsum2
    sum2 += parsum2
#print(sum1)
#aocd.submit(sum1)
print(sum2)
aocd.submit(sum2)