n = int(input())
a = list(map(int, input().split()))
if n != 1:
    boo = False
    if a[0] > a[1]:
        boo = True
    ans = 1
    maxi = -1
    
    for i in range(n - 1):
        gian = True
        if boo:
            if a[i] > a[i + 1]:
                ans += 1
            else:
                maxi = max(ans, maxi)
                #print(maxi)
                ans = 1
                if a[i] < a[i + 1]:
                    ans = 2
                    boo = True
                    gian = False
            
            if gian:
                boo = False
        else:
            if a[i] < a[i + 1]:
                ans += 1
            else:
                maxi = max(ans, maxi)
                #print(maxi)
                ans = 1
                if a[i] > a[i + 1]:
                    ans = 2
                    boo = False
                    gian = False
        
            if gian:
                boo = True
    maxi = max(ans, maxi)
else:
    maxi = 1
print(maxi)