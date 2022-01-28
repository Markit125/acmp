import math
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
R = int(input())
s = int(input())
r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
if r > 2 * R:
    S = 2 * math.pi * R ** 2
else:
    alpha = math.acos(r/2/R)
    S = 2 * R ** 2 * (math.pi - alpha + math.sin(alpha) * math.cos(alpha))
if S > s:
    print('YES')
else:
    print('NO')
