c, n = map(int, input().split())
if n == 1:
    print(c)
else:
    m = 1
    x = 1
    k = 2
    a = [1] * c
    a[n - 1] = 2
    p = False
    while True:
        for i in range(m, len(a), k):
            if a[i] != 2:
                a[i] = 0
                x += 1
            else:
                p = True
                break
        k += 2
        m *= 2
        if p:
            break
    print(x)