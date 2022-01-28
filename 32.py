a = int(input())
b = int(input())
aans = ''
bans = ''
if a < 0:
    a = str(a)
    a = a[1:]
    aans = '-'
if b < 0:
    b = str(b)
    b = b[1:]
    bans = '-'   
b = str(b)
a = str(a)
 
for k in range(len(a) - 1):
    for i in range(len(a) - k - 1):
        if int(a[i]) < int(a[i + 1]):
            a = a[:i] + a[i + 1] + a[i] + a[i + 2:]
         
for k in range(len(b) - 1):
    for i in range(len(b) - k - 1):
        if int(b[i]) < int(b[i + 1]):
            b = b[:i] + b[i + 1] + b[i] + b[i + 2:]
             
if bans == '':
    b = b[::-1]
    z = ''
    k = 0
    for i in range(len(b)):
        if b[i] == '0':
            z += '0'
            k += 1
    b = b[k:]
    if len(b) > 1:
        b = b[0] + z + b[1:]
    elif len(b) == 1:
        b = b[0] + z
    else:
        b = '0'
 
if aans == '-':
    a = a[::-1]
    z = ''
    k = 0
    for i in range(len(a)):
        if a[i] == '0':
            z += '0'
            k += 1
    a = a[k:]
    if len(a) > 1:
        a = a[0] + z + a[1:]
    elif len(a) == 1:
        a = a[0] + z
    else:
        a = '0'

		
    
     
     
aans = int(aans + a)
bans = int(bans + b)
 
print(aans - bans)  