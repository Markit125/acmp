n=int(input())
a=list(map(int,input().split()))
b=[0]*201
for i in range(n):
    b[a[i]+100]+=1
for i in range(201):
    for k in range(b[i]):
        print(i-100,end=' ')
        