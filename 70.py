s = input()
k = int(input())
if k > 0:
    if len(s) * k < 1023:
        print(s * k)
    else:
        s = s * (1023 // len(s) + 1)
        print(s[:1023])
        
        

else:
    k = -k
    if len(s) % k == 0:
        a = s[:len(s) // k]
        if a * k == s:
            if len(s) > 1023:
                print(s[:1023])
            else:
                print(a)
        else:
            print('NO SOLUTION')
    else:
        print('NO SOLUTION')