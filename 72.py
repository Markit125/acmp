a = list(input())
s = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(a) - 1, 0, -1):
    if s.index(a[i]) > s.index(a[i - 1]):
        l = ''
        for k in range(i, len(a)):
            l += a[k]

        for n in s[s.index(a[i - 1]):]:
            if n in l:

                for k in range(i, len(a)):
                    if a[k] == n:
                        a[k] = 0
                        a.remove(0)
                        a.insert(i - 1, n)
                        break
                break
        break
l = ''
for k in range(i, len(a)):
    l += a[k]
l = sorted(l)
n = a[:i] + l
l = ''
for k in range(len(n)):
    l += n[k]
print(l)