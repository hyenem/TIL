from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sx, sy, tsd = map(lambda x: int(x)-1, input().split())
ex, ey, ted = map(lambda x: int(x)-1, input().split())
sd = (1, 3, 2, 0)[tsd]
ed = (1, 3, 2, 0)[ted]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

visited = [[[0]*4 for _ in range(M)] for _ in range(N)]
q = deque([(0, sx, sy, sd)])
visited[sx][sy][sd]=1
while q:
    t, x, y, d = q.popleft()
    if (x, y, d)==(ex, ey, ed):
        print(t)
        break

    for nd in ((d+1)%4, (d+3)%4):
        if visited[x][y][nd]: continue
        visited[x][y][nd]=1
        q.append((t+1, x, y, nd))

    for k in range(1, 4):
        dx, dy = dxdy[d]
        nx, ny = x+k*dx, y+k*dy
        if not(0<=nx<N and 0<=ny<M) or arr[nx][ny]==1: break
        if visited[nx][ny][d]: continue
        visited[nx][ny][d]=1
        q.append((t+1, nx, ny, d))