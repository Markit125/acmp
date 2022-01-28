s = input()
x = int(input())
if x % 2 == 1 or (s == 'Home' and x % 2 == 0):
    print('Yes')
else:
    print('No')