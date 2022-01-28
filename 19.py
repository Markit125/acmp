ls = list(map(str,input().split()))

for i in range(3):
    if ls[i][0] == 'A':
        ls[i] += '1'
    elif ls[i][0] == 'B':
        ls[i] += '2'
    elif ls[i][0] == 'C':
        ls[i] += '3'
    elif ls[i][0] == 'D':
        ls[i] += '4'
    elif ls[i][0] == 'E':
        ls[i] += '5'
    elif ls[i][0] == 'F':
        ls[i] += '6'
    elif ls[i][0] == 'G':
        ls[i] += '7'
    else:
        ls[i] += '8'



field = [[0] * 8 for i in range(8)]
for x in range(8):
    for y in range(8):
        if int(ls[0][2]) - 1 == x or int(ls[0][1]) - 1 == y or int(ls[1][2]) - 1 == x or int(ls[1][1]) - 1 == y:
            field[x][y] = 1
        elif abs(x - y) == abs(int(ls[0][2]) - int(ls[0][1])):
            field[x][y] = 1
        elif abs(x + y) == abs(int(ls[0][2]) + int(ls[0][1])):
            field[x][y] = 1
        elif abs((x - y) * (int(ls[2][2]) - int(ls[2][1]))) == 2:
            field[x][y] = 1

field[int(ls[0][2]) - 1][int(ls[0][1]) - 1] = 9
field[int(ls[1][2]) - 1][int(ls[1][1]) - 1] = 5
field[int(ls[2][2]) - 1][int(ls[2][1]) - 1] = 3

ans = -17

for x in range(8):
    for y in range(8):
        ans += field[x][y]
for i in range(8):
    print(field[i])
print(ans)
