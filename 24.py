n, m = map(int, input().split())
if n < m:
    print(0)
else:
    if m == 0:
        print(1)
    elif m == 1:
        print(n)
    else:
        ans = n - m + 1
        for i in range(1, n):
            if m + m * i - i <= n:
                ans += n - m - m * i + 1 + i
            else:
                break
        print(ans)
