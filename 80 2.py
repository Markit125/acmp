s = input()
p = True
if s[0] in '1234567890-':
    a = s[0]
    d = '1234567890'
    i = 1
    l = len(s)
    #print('0')
    if i < l and (s[i] in d or s[i] in '/*-+'):
        while i < l and s[i] in '1234567890':
            a += s[i]
            i += 1
        #print('1')
        if i < l:
            if s[i] in '/*-+':
                q = s[i]
                i += 1
                if i < l:
                    if s[i] in '1234567890-':
                        #print('2')
                        b = s[i]
                        d = '1234567890'                    
                        i += 1
                        if i < l and (s[i] in d or s[i] == '='):
                            #print('3')
                            while i < l and s[i] in '1234567890':
                                b += s[i]
                                i += 1
                            #print('4')
                            if i < l:
                                #print('86581461')
                                if s[i] == '=':
                                    i += 1
                                    #print('4')
                                    if i < l:
                                        if s[i] in '1234567890-':
                                            c = s[i]
                                            k = i
                                            #print('5')
                                            d = '1234567890'                                    
                                            i += 1
                                            if (i < l and s[i] in d) or i == l:
                                                while i < l and s[i] in '1234567890':
                                                    c += s[i]
                                                    i += 1     
                                                #print('6')
                                                if s[k:] == c:
                                                    p = False
                                                    #print(a + q + b + '==' + c)
                                                    if q == '/' and b == '0':
                                                        print('NO')
                                                    else:
                                                        if bool(eval(str(int(a)) + q + str(int(b)) + '==' + str(int(c)))):
                                                            print('YES')
                                                        else:
                                                            print('NO')
if p:
    print('ERROR')