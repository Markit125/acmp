n, k = map(int, input().split())
c = 0
while k ** c < n:
    c += 1
c -= 1
#print('c =', c)
a = ''
for i in range(c, -1, -1):
    q = k ** i
    a += str(n // q)
    n -= q * (n // q)
#print('a =', a)
p = 1
s = 0
for i in a:
    p *= int(i)
    s += int(i)
print(p - s)