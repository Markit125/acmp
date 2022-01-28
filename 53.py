n, m = map(int, input().split())
a = [0] * 4

for k in range(1, n + 1):
    for i in range(1, m + 1):
        if (k * i) % 5 == 0:
            a[2] += 1
        elif (k * i) % 3 == 0:
            a[1] += 1
        elif (k * i) % 2 == 0:
            a[0] += 1


print('RED :', a[0])
print('GREEN :', a[1])
print('BLUE :', a[2])
print('BLACK :', n * m - sum(a))
        
        
