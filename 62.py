s = input()
p = s[1]
if s[0] == 'A':
    p = '1' + p
elif s[0] == 'B':
    p = '2' + p
elif s[0] == 'C':
    p = '3' + p
elif s[0] == 'D':
    p = '4' + p
elif s[0] == 'E':
    p = '5' + p
elif s[0] == 'F':
    p = '6' + p
elif s[0] == 'G':
    p = '7' + p
elif s[0] == 'H':
    p = '8' + p

if (int(p[0]) + int(p[1])) % 2 == 0:
    print('BLACK')
else:
    print('WHITE')