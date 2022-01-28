maxi = 0
c = 0
for i in range(1016, 7938):
    if i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        if i % 3:
            maxi = i
            c += 1
print(c, maxi)