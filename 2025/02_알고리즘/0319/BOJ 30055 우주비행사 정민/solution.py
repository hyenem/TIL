import heapq
from collections import deque

dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
K, N1, M1, N2, M2 = map(int, input().split())
A, B = map(int, input().split())
gate = [list(map(int, input().split())), list(map(int, input().split()))]
inf = 90001
blackhole = [[[inf]*M1 for _ in range(N1)], [[inf]*M2 for _ in range(N2)]]

bq1 = deque()
bq2 = deque()
for _ in range(K):
    n, x, y = map(int, input().split())
    blackhole[n-1][x][y]=0
    if n==1:
        bq1.append((0, x, y))
    else :
        bq2.append((0, x, y))

while bq1:
    t, x, y = bq1.popleft()
    if x==N1-1 and y==0: nx, ny = 0, 0
    elif x%2==0:
        if y==M1-1: nx, ny = x+1, y
        else : nx, ny = x, y+1
    else :
        if y==0: nx, ny = x+1, y
        else : nx, ny = x, y-1

    if blackhole[0][nx][ny]==inf:
        blackhole[0][nx][ny]=t+1
        bq1.append((t+1, nx, ny))

while bq2:
    t, x, y = bq2.popleft()
    if x == N2 - 1 and y == 0:
        nx, ny = 0, 0
    elif x % 2 == 0:
        if y == M2 - 1:
            nx, ny = x + 1, y
        else:
            nx, ny = x, y + 1
    else:
        if y == 0:
            nx, ny = x + 1, y
        else:
            nx, ny = x, y - 1

    if blackhole[1][nx][ny] == inf:
        blackhole[1][nx][ny] = t + 1
        bq2.append((t + 1, nx, ny))

visited =[[[inf]*M1 for _ in range(N1)], [[inf]*M2 for _ in range(N2)]]
q = [(0, 0, 0, 0)]
visited[0][0][0]=1
while q:
    t, n, x, y = heapq.heappop(q)
    if n==-1 and x==N2-1 and y==M2-1:
        print(t)
        break
    if visited[n][x][y]<t: continue

    if n==0: N, M = N1, M1
    else : N, M = N2, M2

    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if not (0<=nx<N and 0<=ny<M): continue
        if t+1>=blackhole[n][nx][ny]: continue
        if visited[n][nx][ny]>t+1:
            visited[n][nx][ny]=t+1
            heapq.heappush(q, (t+1, n, nx, ny))
            if 0<=nx-gate[n][0]<A and 0<=ny-gate[n][1]<B:
                nnx, nny = gate[-1-n][0]+nx-gate[n][0], gate[-1-n][1]+ny-gate[n][1]
                if visited[-1-n][nnx][nny]>t+4 and t+4<blackhole[-1-n][nnx][nny]:
                    visited[-1-n][nnx][nny]=t+4
                    heapq.heappush(q, (t+4, -1-n, nnx, nny))

else: print('hing...')