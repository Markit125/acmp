n = int(input())
if n == 0:
    print(n)
else:
    i = 0
    ans = 0
    while 2 ** i <= n:
        i += 1
    i -= 1
    for k in range(i, -1, -1):
        if n >= 2 ** k:
            n -= 2 ** k
            ans += 1
    print(ans)