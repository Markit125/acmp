n, k = map(str, input().split())
n = int(n)
k = len(k)
ans = 1
if n != 0:    
    while n >= k and n >= n % k:
        ans *= n
        n -= k
              
print(ans)