s = input()
n = int(input())
if n > 0:
    a = [0] * n
    l = len(s)
    for i in range(n):
        x = input()
        for k in range(l):
            if s[k] != x[k]:
                a[i] += 1
    #print(a)
    x = min(a)
    print(a.count(x))
    for i in range(n):
        if a[i] == x:
            print(i + 1, end = ' ')
else:
    print(0)