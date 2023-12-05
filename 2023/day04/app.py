import aocd
from collections import defaultdict
import re
rx = re.compile(r'[0-9]+')
debug = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
data = debug.split("\n")
data = aocd.get_data().split("\n")
data = [row.split(":")[1] for row in data]
divided = []
for row in data:
    x = row.split("|")
    divided.append(x)
#Task 1
sum1 = 0
for winning, numbers in divided:
    s = 0
    for w in rx.finditer(winning):
        for n in rx.finditer(numbers):
            if w.group() == n.group():
                if s == 0:
                    s = 1
                else:
                    s*=2
    sum1 += s
#27454
print(sum1)
#data = aocd.get_data().split("\n")
#print(data)

#aocd.submit(sum1)

def pointsFromCars(card):
    winning = card[0]
    numbers = card[1]
    s = 0      
    for w in rx.finditer(winning):
        for n in rx.finditer(numbers):
            if w.group() == n.group():
                
                s+=1
    return s
#Task 2
copies = 0
d = {}
#Each card weights 1 in the beginning
for i in range(len(divided)):
    d[i] = 1
for i,card in enumerate(divided):
    copies += 1
    points = pointsFromCars(card)
    j = i + 1
    times = 0
    while times<points and j<len(divided):
        d[j] += d[i]
        j+=1
        times += 1
sum2 = 0
for i in d.values():
    sum2 += i
print(sum2)
#6857330
aocd.submit(sum2)