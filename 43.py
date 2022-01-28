ls = list(map(str, input().split('1')))
maxi = 0
for i in range(len(ls)):
    if len(ls[i]) > maxi:
        maxi = len(ls[i])
print(maxi)

