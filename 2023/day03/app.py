import aocd
valid_symbols = "!@#$%^&*()_-+/|\={}[]"
def getNumbers(s):
    tn = {}
    n = []
    start = False
    index = 0
    for i,c in enumerate(s):
        if c.isdigit():
            if not start:
                tn[i] = c
                start = True
                index = i
                continue
            else:
                tn[index] = tn[index]+ c
        else: 
            if start:
                start = False
    return tn
def getGears(s):
    tn = []
    for i,c in enumerate(s):
        if c == "*":
            tn.append(i)
    return tn

def IsPartNumber(nrrow, pos, val, data):
    #check left right
    if pos>0:
        if data[nrrow][pos-1] in valid_symbols:
            return True
    if pos+len(val)<len(data[0]):
        if data[nrrow][pos+len(val)] in valid_symbols:
            return True
    values_to_check = range(max(pos-1,0),min(pos+len(val)+1,len(data[0])))
    #top
    if nrrow>0:
        for value in values_to_check:
            if data[nrrow-1][value] in valid_symbols:
                return True
    #bottom
    if nrrow+1 < len(data):
        for value in values_to_check:
            if data[nrrow+1][value] in valid_symbols:
                return True
    return False
#data = aocd.get_data(day=3, year=2023)
data = aocd.get_data(day=3, year=2023)
data = data.split("\n")
sum1 = 0
n = [getNumbers(row) for row in data]
gears = [getGears(row) for row in data]
for nrrow, row in enumerate(n):
    for key, val in row.items():
        if IsPartNumber(nrrow, key, val, data):
            sum1 += int(val)
            #print(nrrow,val)
print(sum1)
sum2= 0
for nrrow, rowgear in enumerate(gears):
    for gear in rowgear:
        nums = []
        #right
        if gear +1 < len(data[0]):
            if gear + 1 in n[nrrow].keys():
                nums.append(n[nrrow][gear + 1])
        if gear - 1 < len(data[0]):
            i = gear
            while i>0 and data[nrrow][i-1].isdigit():
                i-=1
            if i in n[nrrow].keys():
                nums.append(n[nrrow][i])
        values_to_check = range(max(gear-1,0),min(gear+2,len(data[0])))
        #bottom
        if nrrow>0:
            for num in n[nrrow-1].keys():
                for rn in range(num, num+ len(n[nrrow-1][num])):
                    if rn in values_to_check:
                        nums.append(n[nrrow-1][num])
        #tom
        if nrrow+1 < len(data):
            for num in n[nrrow+1].keys():
                for rn in range(num, num+ len(n[nrrow+1][num])):
                    if rn in values_to_check:
                        nums.append(n[nrrow+1][num])
        nums = list(set(nums))
        if len(nums)==2:
            nr = int(nums[0]) * int(nums[1])
            sum2 += nr
print(sum2)
aocd.submit(sum2)