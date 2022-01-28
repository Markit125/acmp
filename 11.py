k, n = map(int, input().split())
a = [0 * i for i in range(n + 1)]
a[n] = 1
for j in range(n - 1, -1, -1):
    i = 0
    while i < k and j + i < n:
        a[j] += a[j + i + 1]
        i += 1
print(a[0])
