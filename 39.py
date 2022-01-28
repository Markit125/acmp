n = int(input())
ls = list(map(int, input().split()))
a = ls
ans = 0
i = ls.index(max(ls))
l = 0
while i < n:
    ans += (i + 1 - l) * ls[i]
    l = i + 1
    a = a[a.index(ls[i]) + 1:]
    if len(a) != 0:
        i = ls.index(max(a), i + 1, n)
    else:
        break
    
    #print(i)
print(ans)
    