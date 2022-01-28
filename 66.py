c = input()
s = 'qwertyuiopasdfghjklzxcvbnm'
if s.index(c) < 25:
    print(s[s.index(c) + 1])
else:
    print('q')