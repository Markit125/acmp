n, c, p = map(int, input().split())
a = []
for i in range(n + 1):
    x, y = (map(int, input().split()))
    a.append(x)
    a.append(y)
#print(a)

s = c * ((a[-2] - a[0]) ** 2 + (a[-1] - a[1]) ** 2) ** .5
#print('s =', s)

for i in range(2, 2 * n, 2):
    s += c * ((a[0] - a[i]) ** 2 + (a[1] - a[i + 1]) ** 2) ** .5
    #print('s =', s)

if s <= p:
    print('YES')
else:
    print('NO')