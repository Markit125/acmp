x1, y1, x2, y2 = map(int, input().split())
xa, ya = map(int, input().split())
if x1 == x2:
    xb = 2 * x1 - xa
    yb = ya
else:
    yb = 2 * y1 - ya
    xb = xa
print(xb, yb)