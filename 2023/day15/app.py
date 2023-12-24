import aocd


data = aocd.get_data(day=15)

debug="""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
#data= debug
data = data.split(",")

def Hash(s):
    h = 0
    for c in s:
        h=((h+ord(c))*17)%256
    return h

sum1 = 0
h = []
for s in data:
    sum1+=Hash(s)
    if '=' in s:
        h.append(Hash(s.split("=")[0]))
    else:
        h.append(Hash(s[:-1]))
d = {}
for i,s in enumerate(data):
    k = ""
    if '=' in s:
        k = s.split("=")[0]
    else:
        k = s[:-1]
    if h[i] not in d.keys():
        d[h[i]] = {}

    if k in d[h[i]].keys() and '-' in s:
        del d[h[i]][k]
    elif '=' in s:
        d[h[i]][k] = s.split("=")[1]

sum2 = 0
#print(d)
for k in sorted(d.keys()):
    pos = 0
    for k2 in d[k].keys():
        sum2 += (int(k)+1)*(pos + 1) * ( int(d[k][k2]))
        #print(int(k)+1,pos+1,int(d[k][k2]))
        pos+=1
print(sum2)
    