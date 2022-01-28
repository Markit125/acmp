n = int(input())
ans = 0
for i in range(n):
     x, y, x1i, y1i, x2i, y2i, x3i, y3i, x4i, y4i = map(float, input().split())
     
     if x1i == x2i or x2i == x3i:
          x1 = min(x1i, x2i, x3i, x4i)
          x2 = x1
          x3 = max(x1i, x2i, x3i, x4i)
          x4 = x3
          y1 = min(y1i, y2i, y3i, y4i)
          y4 = y1
          y2 = max(y1i, y2i, y3i, y4i)
          y3 = y2
                         
          if x >= x1 and y <= y2 and x <= x3 and y >= y4:
               ans += 1
     

     else:
          x1 = min(x1i, x2i, x3i, x4i)
          x3 = max(x1i, x2i, x3i, x4i)
     
          y2 = max(y1i, y2i, y3i, y4i)
          y4 = min(y1i, y2i, y3i, y4i)
     
          if y2 == y2i:
               x2 = x2i
          elif y2 == y4i:
               x2 = x4i
          elif y2 == y3i:
               x2 = x3i
          else:
               x2 = x1i
     
          if y4 == y2i:
               x4 = x2i
          elif y4 == y4i:
               x4 = x4i
          elif y4 == y3i:
               x4 = x3i
          else:
               x4 = x1i
          
          if x1 == x1i:
               y1 = y1i
          elif x1 == x2i:
               y1 = y2i
          elif x1 == x3i:
               y1 = y3i
          else:
               y1 = y4i
          
          if x3 == x1i:
               y3 = y1i
          elif x3 == x2i:
               y3 = y2i
          elif x3 == x3i:
               y3 = y3i
          else:
               y3 = y4i
    
          if (x - x1) * (y2 - y1) / (x2 - x1) + y1 > y or (x - x1) * (y2 - y1) == (x2 - x1) * (y - y1):
               if (x - x2) * (y3 - y2) / (x3 - x2) + y2 > y or (x - x2) * (y3 - y2) == (x3 - x2) * (y - y2):
                    if (x - x3) * (y4 - y3) / (x4 - x3) + y3 < y or (x - x3) * (y4 - y3) == (x4 - x3) * (y - y3):
                         if (x - x4) * (y1 - y4) / (x1 - x4) + y4 < y or (x - x4) * (y1 - y4) == (x1 - x4) * (y - y4):
                              ans += 1
                         
print(ans)
