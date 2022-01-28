w, h = map(int, input().split())
n = int(input())
mol = [[0] * w for i in range(h)]
ans = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0

for i in range(n):
    x, y, x1, y1 = map(int, input().split())
    if not (x >= x2 and x1 <= x3 and y >= y2 and y1 <= y3):
        for a in range(x, x1):
            for b in range(y, y1):
                if mol[a][b] == 0:
                    mol[a][b] = 1
                    ans += 1
        x2 = x
        x3 = x1
        y2 = y
        y3 = y1
       
print(w * h - ans)