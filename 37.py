from math import sqrt
n, q = input().split()
n = int(n)
q = float(q)
c = 0
for i in range(n):
    x, y, x1, y1 = map(int, input().split())
    if q * (x ** 2 + y ** 2) >= x1 ** 2 + y1 ** 2:
        c += 1
if c == n:
    print('Yes')
else:
    print('No')