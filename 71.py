n = int(input())
a = list(map(int, input().split()))
b = [0] * n
b[0] = -1
s = sum(a)
for q in range(2 ** n):
    b[0] += 1
    for i in range(n - 1):
        if b[i] == 2:
            b[i] = 0
            b[i + 1] += 1        
    x = 0
    y = 0 
    for i in range(n):
        if b[i] == 0:
            x += a[i]
        else:
            y += a[i]
    if abs(x - y) < s:
        s = abs(x - y)   
print(s)
    