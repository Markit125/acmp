x, y, r = map(int, input().split())
x1, y1, r1 = map(int, input().split())
if x1 == x and y1 == y and r1 != r:
    print('NO')
else:
    c = (x1 - x) ** 2 + (y1 - y) ** 2
    s = (r1 + r) ** 2
    if c + r1 < r or c + r < r1:
        print('NO')
    elif c <= s:
        print('YES')
    else:
        print('NO')