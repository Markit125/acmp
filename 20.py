n = int(input())
ls = list(map(int, input().split()))
if n != 1:
    maxi = 0
    boo = False
    if ls[0] > ls[1]:
        boo = True
        
    ans = 1  
    c = 0
    for i in range(n - 1):
        gant = True
        if boo:
            
            if ls[i] > ls[i + 1]:
                ans += 1
            else:
                maxi = max(maxi, ans)
                ans = 1
                if ls[i] != ls[i + 1] and i + 3 <= n:
                    
                    if ls[i + 1] > ls[i + 2]:
                        ans += 1
                        boo = True
                        gant = False
                    
    
            if gant:
                boo = False
            
        else:
            
            if ls[i] < ls[i + 1]:
                ans += 1            
            else:
                maxi = max(maxi, ans)     
                ans = 1
                if ls[i] != ls[i + 1] and i + 3 <= n:
                    if ls[i + 1] < ls[i + 2]:
                        ans += 1
                        boo = False
                        gant = False
            if gant:
                boo = True
                
    maxi = max(maxi, ans)
else:
    maxi = 1
print(maxi)
            