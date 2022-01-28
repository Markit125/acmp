n = int(input())

for i in range(n):
    y, x = map(int, input().split())
    
    b = []
    for k in range(y):
        a = list(map(int, input().split()))
        b.append(a)
    boo = False
    if not (x < 2 or y < 2):
        
        for w in range(x - 1):
            for q in range(y - 1):
                #print(q, w)
                if b[q][w] == b[q + 1][w]:
                    if b[q][w] == b[q][w + 1]:
                        if b[q][w] == b[q + 1][w + 1]:
                            boo = True
                            break
            if boo:
                break    
    if boo:
        print('NO')
    else:
        print('YES')
                    