k = int(input())
a = []
for i in range(k):
    ls = list(map(int, input().split()))
    n = ls[0]
    m = ls[1]
    d = 19 * m + (n + 239) * (n + 366) / 2
    a.append(int(d))
    
for i in range(k):
    print(a[i])