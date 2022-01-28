ls = list(map(int, input().split()))
n = ls[0]
m = ls[1]
s = input()
b = False

for i in range(n - m):
    if s[i:m + i] in s[i + 1:]:
        b = True
        break

if b:
    print('YES')
else:
    print('NO')