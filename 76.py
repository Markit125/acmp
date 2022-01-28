n = int(input())
b = []
for i in range(n):
    a = list(map(str, input().split()))
    a[0] = float(a[0][:2] + '.' + a[0][3:])
    a[1] = float(a[1][:2] + '.' + a[1][3:])
    b.append(a)
m = 0
for i in range(n):
    s = 0
    t = b[i][0]
    for k in range(n):
        if b[k][0] <= t:
            if b[k][1] >= t:
                s += 1
    if s > m:
        m = s
print(m)