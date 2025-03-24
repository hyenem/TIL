N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
K = int(input())
hole = [tuple(map(int, input().split())) for _ in range(K)]
hole.sort()
idx = 0
maxdepth = 0

holeidx = []
height = []
if points[1][0]!=0:
    start, end = 2, N
else : start, end = 1, N-1

for i in range(start, end, 2):
    if idx<K and points[i][0]==hole[idx][0] and points[i][1]==hole[idx][1]:
        holeidx.append(len(height))
        idx += 1

    h = points[i][1]
    maxdepth = max(maxdepth, h)
    w = points[i+1][0]-points[i][0]
    height.append([h, w])

N = len(height)
h = 0
water = [maxdepth]*N
idx = 0
for i in range(N):
    if idx<K and i==holeidx[idx]:
        h = height[i][0]
        idx += 1
    h = min(h, height[i][0])
    water[i] = min(water[i], height[i][0]-h)

h = 0
idx = K-1
for i in range(N-1, -1, -1):
    if idx<K and i==holeidx[idx]:
        h = height[i][0]
        idx -= 1
    h = min(h, height[i][0])
    water[i] = min(water[i], height[i][0]-h)

ans = 0
for i in range(N):
    ans += water[i]*height[i][1]
print(ans)