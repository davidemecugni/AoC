import aocd
import re
rx = re.compile(r'[0-9]+')
data = aocd.get_data(day=7,year=2023)
debug = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
#data = debug
data = data.splitlines()
value_dict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
value_dict_pt_2 = {'J':1, '1':2, '2':3, '3':4, '4':5, '5':6, '6':7, '7':8, '8':9,'9': 10, 'T': 11, 'Q': 12, 'K': 13, 'A': 14}
def GetOrderingPowerPt1(hand):
    s = 0
    for i in range(len(hand)):
        s += value_dict[hand[len(hand)-1-i]]*14**i
    return s
def GetOrderingPowerPt2(hand):
    s = 0
    for i in range(len(hand)):
        s += value_dict_pt_2[hand[len(hand)-1-i]]*14**i
    return s
def GetValue(hand):
    hand = hand.split(" ")
    hand = hand[0]
    d = {}
    for c in hand:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
    if 5 in d.values():
        return 10**70 + GetOrderingPowerPt1(hand)
    if 4 in d.values():
        return 10**60 + GetOrderingPowerPt1(hand)
    if 3 in d.values():
        if 2 in d.values():
            return 10**50+GetOrderingPowerPt1(hand)
        else:
            return 10**40 + GetOrderingPowerPt1(hand)
    couples = 0
    for n in d.values():
        if n == 2:
            couples += 1
    if couples == 2:
        return 10**30 + GetOrderingPowerPt1(hand)
    if couples == 1:
        return 10**20 + GetOrderingPowerPt1(hand)
    return 10**10+GetOrderingPowerPt1(hand)

data = sorted(data, key=GetValue)
sum1 = 0
for i,row in enumerate(data):
    bid = row.split(" ")
    bid = int(bid[1])
    sum1 += (i+1) * bid
print(sum1)

def GetValuePart2(hand):
    hand = hand.split(" ")
    hand = hand[0]
    d = {}
    for c in hand:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
    if 'J' in d.keys():
        nr_j = d['J']
        if nr_j == 5:
            return 10**70 + GetOrderingPowerPt2(hand)
        del d['J']
        keys = list(d.keys())
        maxk = keys[0]
        maxv = 0
        for k in keys:
            if d[k]>maxv:
                maxv = d[k]
                maxk = k
        d[maxk] += nr_j
    
    if 5 in d.values():
        return 10**70 + GetOrderingPowerPt2(hand)
    if 4 in d.values():
        return 10**60 + GetOrderingPowerPt2(hand)
    if 3 in d.values():
        if 2 in d.values():
            return 10**50+GetOrderingPowerPt2(hand)
        else:
            return 10**40 + GetOrderingPowerPt2(hand)
    couples = 0
    for n in d.values():
        if n == 2:
            couples += 1
    if couples == 2:
        return 10**30 + GetOrderingPowerPt2(hand)
    if couples == 1:
        return 10**20 + GetOrderingPowerPt2(hand)
    return 10**10+GetOrderingPowerPt2(hand)

data = sorted(data, key=GetValuePart2)
sum2 = 0
for i,row in enumerate(data):
    bid = row.split(" ")
    bid = int(bid[1])
    sum2 += (i+1) * bid
print(sum2)
#aocd.submit(sum)