ch = [0] * 10
t = list(input().split(':'))
t2 = list(input().split(':'))
for i in range(3):
    t[i] = int(t[i])
    t2[i] = int(t2[i])

while t != t2:
    for i in range(3):
        ch[t[i] // 10] += 1
        ch[t[i] % 10] += 1
    t[2] += 1
    if t[2] > 59:
        t[2] = 0
        t[1] += 1
    if t[1] > 59:
        t[1] = 0
        t[0] += 1
    if t[0] > 23:
        t[0] = 0
        


for i in range(3):
    ch[t[i] // 10] += 1
    ch[t[i] % 10] += 1
    
    
    
for i in range(10):
    print(ch[i])
    



