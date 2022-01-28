from math import sqrt, ceil
n = int(input())
if n % 2 == 0:
    i = n + 1
else:
    i = n + 2
c = 0
while i < 2 * n:
    w = True
    s = ceil(sqrt(i))
    for k in range(3, s + 1):
        if i % k == 0:
            w = False
            break
    if w:
        c += 1
    
    i += 2
print(c)