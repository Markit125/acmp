s, p = map(int, input().split())
for i in range(s):
    if i * (s - i) == p:
        s = s - i
        p = i
        break
print(i, s)