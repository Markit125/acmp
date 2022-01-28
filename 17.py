n = int(input())
st = []
ans = 0
its = True
sam = False
ls = list(map(int,input().split()))
st.append(ls[0])
for i in range(1, n - 1):

    if not its:
        st.append(buf)
    its = True
    st.append(ls[i])
    #print(n - 1, '%', i, '=', (n - 1) % i, 'df')
    #print(ls[0], ls[i])
    if ls[0] == ls[i] and (n - 1) % i == 0:
        #print('here')
        buf = st[-1]
        #print(st)
        del st[-1]

        #print(st)
        k = i
        c = 0

        for p in range(n - 1):
            #print(c)
            if c == k:
                c = 0
            if ls[p] != st[c]:
                #print('False')
                its = False
                break
            c += 1

        if its:
            #print('True')
            sam = True
            break

if not sam:
    if ls[0] == ls[-1]:
        k = len(ls) - 1
print(k)