import re
with open("data.txt") as f: 
    s = f.read()
numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
for i in range(10):
    numbers.append(str(i))
def strToNum(number):
    n = numbers.index(number)
    if n>10:
        return n -10
    return n
s = s.split("\n")
sum = 0
for row in s:
    d = {}
    for number in numbers:
        found = 1
        start = 0
        while found != -1:
            found = row.find(number, start)
            if found != -1:
                start += found + len(number)
                d[found] = strToNum(number)
    d = sorted(d.items())
    sum += d[0][1]*10 + d[-1][1]
print(sum)


