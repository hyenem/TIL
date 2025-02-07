import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if (x1, y1)==(x2, y2):
        if r1==r2 : print(-1)
        else : print(0)
    else:
        d = math.sqrt((x1-x2)**2 +(y1-y2)**2)
        if abs(r2-r1)d < r1 + r2