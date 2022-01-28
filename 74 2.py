c, n = map(int, input().split())
if n == 1:
    print(c)
else:
    p = True
    x = 0
    while p:  
        if n % 2 != 0:
            x += c // 2
            c -= c // 2
        else:
            p = False
            x += n // 2
        n -= n // 2
    print(x)