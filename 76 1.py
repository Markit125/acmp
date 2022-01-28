n = int(input())
b = []
for i in range(n):
    q, w = list(map(str, input().split()))
    q = float(q[:2] + '.' + q[3:])
    w = float(w[:2] + '.' + w[3:])
    b.append(q)
    b.append(w)
m = 0
for i in range(0, n * 2, 2):
    s = 0
    t = b[i]
    #print(i)
    for k in range(0, n * 2, 2):
        if b[k] <= t:
            if b[k + 1] >= t:
                s += 1
    if s > m:
        m = s
print(m)