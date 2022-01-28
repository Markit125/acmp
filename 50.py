s = input()
p = input()
ans = 0
ls = []
ls.append(p)
for i in range(len(p)):
    for k in range(len(s) - len(p) + 1):
        if p == s[k:k + len(p)]:
            ans += 1    
    o = False
    for g in range(len(p)):
        if p in ls:
            p = p[-1] + p[:-1]
        else:
            o = True
            break
    if o:
        ls.append(p)
    else:
        break
    #print(ls)
print(ans)