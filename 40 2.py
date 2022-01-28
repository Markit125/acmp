n = int(input())

bu = False
a = [1]
for i in range(n):
    k = 0
    while k < len(a):
        #print(a)
        a[k] *= 2
        if bu:
            a[k] += 1
            bu = False
        if a[k] > 9:
            if k == len(a) - 1:
                a.append(0)                
            bu = True
            a[k] -= 10
        k += 1
        #print(a)
if bu:
    a[-1] += 1
st = ''
for i in range(len(a) - 1, -1, -1):
    st += str(a[i])
print(int(st))
        