import aocd
def IsComp(dic):
    test = {"blue":14,"green":13,"red":12}
    """     
    if len(dic) > 3:
        return False
    for d in dic.keys():
        if d not in test.keys():
            return False 
    """
    for d in dic.keys():
        if dic[d]>test[d]:
            return False
    return True

""" with open("data.txt") as f: 
    s = f.read()
"""
s = aocd.get_data()
s = s.split("\n")

d = []
for i,row in enumerate(s) :
    dic = {}

    row = row.split(":")[1]
    #print(row)
    #row = re.split(';|,', row)
    row = row.split(";")
    for subrow in row:
        subrow = subrow.split(",")
        for i in range(len(subrow)):
            subrow[i] = subrow[i][1:]
        subdic = {}

        for r in subrow:
            s = r.split(" ")
            subdic[s[1]] = int(s[0])
        for subcol in subdic.keys():
            if subcol not in dic.keys():
                dic[subcol] = subdic[subcol]
            else:
                if subdic[subcol] > dic[subcol]:
                    dic[subcol] = subdic[subcol]              
    d.append(dict(sorted(dic.items())))
sum1 = 0
sum2 = 0
""" for i,el in enumerate(d):
    print(i+1,el) """
for i, el in enumerate(d):
    t = 1
    for key,val in el.items():
        t *= val
    sum2 += t
    if IsComp(el):
        sum1 += 1+i

print(f"1) {sum1}")
print(f"2) {sum2}")
aocd.submit(sum2)