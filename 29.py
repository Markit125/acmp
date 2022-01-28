n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(0)
else:
    b = [0 for i in range(n)]
    b[1] = abs(a[1] - a[0])

    for i in range(2, n):
        b[i] = min(3 * abs(a[i] - a[i - 2]) + b[i - 2], abs(a[i] - a[i - 1]) + b[i - 1])
    #print(b)
    print(b[-1])
