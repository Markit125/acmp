
n = int(input())
ans = 1
lvl = 0
buf = -1
a = 0
while True:
    le = [n, 0]
    #le.append(-1)
    for i in range(lvl):
        le.insert(-1, 0)
    lvl += 1
    while True:
        #a = 0
        print(le)
        for i in range(len(le) - 1):
            if le[i + 1] + 2 >= le[i]:
                print(buf, '___', i)
                if buf >= 0 and le[buf] >= le[buf + 1] + 2 and buf != i != buf + 1:
                    print('======', buf,'<>', i,'========')
                    print(le)
                    le[i] += 1
                    le[buf] -= 1
                    print(le)
                    buf = -1
                    if le[-1] != 0:
                        print(ans,'bonus++', le)
                        ans += 1
                    
                    
                elif buf == -1:
                    print('======================',i,'=========================')
                    buf = i

                    
            elif le[i + 1] + 2 < le[i]:
                le[i] -= 1
                le[i + 1] += 1
                a -= 1
                
                print('====')
                if le[-1] != 0:
                    print(ans,'++', le)
                    ans += 1
            a += 1
            
                    
            
        if a == 2:
            a = 0
            break

    if le[-1] == 0:
        break

print(ans)

    
