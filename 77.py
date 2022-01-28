n, k = map(int, input().split())
c = 0
for i in range(1, n + 1):
    s = str(bin(i))
    if s.count('0') - 1 == k:
        c += 1
print(c)
