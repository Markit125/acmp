from math import ceil
m = int(input())
a = '2'
d = list(map(int, input().split()))
s = max(d)
n = 3
while s > len(a):
    b = True
    for i in range(2, ceil(n ** .5) + 1):
        if n % i == 0:
            b = False
    if b:
        a += str(n)
    n += 1
s = ''
for i in range(m):
    s += a[d[i] - 1]
print(s)