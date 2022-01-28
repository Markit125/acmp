from math import cos, radians, tan
n, a = map(int, input().split())
if a / 2 * (1 / cos(radians(90 * (n - 2) / n)) - tan(radians(90 * (n - 2) / n))) < 1:
    print('YES')
else:
    print('NO')