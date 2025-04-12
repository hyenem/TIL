from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='S':
            sx, sy = i, j
            arr[i][j]='.'

dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

q = deque([(sx, sy, -1, 0)])
nq = []
visited = [[[0]*4 for _ in range(M)] for _ in range(N)]
while q:
    x, y, d, t= q.popleft()
    if arr[x][y]=='C':
        nq.append((x, y, d, t))

    for nd in range(4):
        if d==nd: continue
        dx, dy = dxdy[nd]
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M): continue
        if visited[nx][ny][nd]: continue
        if arr[nx][ny]=='#': continue
        visited[nx][ny][nd]=1
        q.append((nx, ny, nd, t+1))

ans = -1
for sx, sy, d, t in nq:
    q = deque([(sx, sy, d, t)])
    visited = [[[0]*4 for _ in range(M)] for _ in range(N)]
    while q:
        x, y, d, t = q.popleft()
        if arr[x][y]=='C' and (sx, sy)!=(x, y):
            if ans == -1:
                ans = t
            else:
                ans = min(ans, t)
            break

        for nd in range(4):
            if nd==d: continue
            dx, dy = dxdy[nd]
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M) or visited[nx][ny][nd] or arr[nx][ny]=='#': continue
            visited[nx][ny][nd]=1
            q.append((nx, ny, nd, t+1))

print(ans)