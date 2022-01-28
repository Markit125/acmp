m = int(input())
a = []
for i in range(m):
    a.append(input())

n = int(input())
if m != 0:
    d = [0] * n
    
    for u in range(n):
        b = list(map(str, input().split()))
        if len(b[0]) > len(b[1]):
            h = 1
        else:
            h = 0
        for q in range(m):
            bo = True
            
            for k in range(len(b[h])):
                if b[1][k] != b[0][k]:
                    s = b[1][:k]
                    c = s.count('.')
                    
                    l = 0
                    for e in range(len(a[q])):
                        if a[q][e] == '.':
                            l += 1
                            f = e
                            if l == c:
                                break
                    S = a[q][f + 1:]
                    if '.' in S:
                        S = S[:S.index('.')]
                    
                    x = int(S)
                    if x != 0:
                        w = ''
                        st = 0
                        while 2 ** st <= x:
                            #print('2')
                            st += 1
                        st -= 1
                        
                        while st >= 0:
                            #print('3')
                            #print('x =', x)
                            
                            if x // 2 ** st == 1:
                                w += '1'
                                x -= 2 ** st
                            else:
                                w += '0'
                            #print('w =', w)
                            st -= 1
                            
                        if len(w) < 8:
                            w = '0' * (8 - len(w)) + w
                            
                    else:
                        w = '00000000'
                    
                    #====================================
                        
                    
                                    
                    l = 0
                    
                    for e in range(len(b[0])):
                        if b[0][e] == '.':
                            l += 1
                            f = e
                            if l == c:
                                break
                    S = b[0][f + 1:]
                    if '.' in S:
                        S = S[:S.index('.')]               
                    x = int(S)
                    #print('gant =',x)
                    if x != 0:
                        s0 = ''
                        st = 0
                        while 2 ** st <= x:
                            #print('5')
                            st += 1
                        st -= 1
                        
                        while st >= 0:
                            #print('6')
                            
                            if x // 2 ** st == 1:
                                s0 += '1'
                                x -= 2 ** st
                            else:
                                s0 += '0'
                            #print('gx =', x)
                            #print('s0 =', s0)
                            st -= 1
                            
                        if len(s0) < 8:
                            s0 = '0' * (8 - len(s0)) + s0
                        #print('s0 =', s0)
                            
                    else:
                        s0 = '00000000'
                        
                    
                    #=====================================
                    
                    
                    l = 0
                    for e in range(len(b[1])):
                        if b[1][e] == '.':
                            l += 1
                            f = e
                            if l == c:
                                break
                    S = b[1][f + 1:]
                    if '.' in S:
                        S = S[:S.index('.')]               
                    x = int(S)
                    #print('gant2 =', x)
                    if x != 0:
                        s1 = ''
                        st = 0
                        while 2 ** st <= x:
                            #print('5')
                            st += 1
                        st -= 1
                        
                        while st >= 0:
                            #print('6')
                            
                            if x // 2 ** st == 1:
                                s1 += '1'
                                x -= 2 ** st
                            else:
                                s1 += '0'
                            #print('gx =', x)
                            #print('s1 =', s1)
                            st -= 1
                            
                        if len(s1) < 8:
                            s1 = '0' * (8 - len(s1)) + s1
                        #print('s1 =', s1)
                            
                    else:
                        s1 = '00000000'
                        
                    #===========================================
                    
                    r0 = ''
                    r1 = ''
                    for i in range(8):
                        if w[i] == s0[i] == '1':
                            r0 += '1'
                        else:
                            r0 += '0'
                    #print('=====')
                    for i in range(8):
                        if w[i] == s1[i] == '1':
                            r1 += '1'
                        else:
                            r1 += '0'
                    #print(w, '\n', r0, '\n', r1)
                    if r1 == r0:
                        continue
                    else:
                        bo = False
                        break
            #print('=====1')
            if bo:
                d[u] += 1
            #print(a[q])
    #print('csdcsdc')
    for i in range(n):
        print(d[i])
else:
    for u in range(n):
        b = list(map(str, input().split()))    
    print('0\n' * n)