from math import ceil
k = int(input())
a = [0, 2]
c = 0
n = 3
while True:
    bo = True
    for i in range(2, ceil(n ** .5) + 1):
        if n % i == 0:
            bo = False
            break
    if bo:
        a.append(n)
        #print('indx', a.index(n))
        if a.index(n) in a:
            c += 1
            if c == k:
                s = n
                break
    n += 1
    #print(a)
print(s)
    