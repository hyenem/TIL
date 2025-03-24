from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
tomato = M*N*H
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == -1:
                tomato -=1
            elif arr[i][j][k]==1:
                tomato-=1
                q.append((0, i, j, k))

dx = (-1, 0, 1, 0, 0, 0)
dy = (0, 0, 0, 0, -1, 1)
dz = (0, 1, 0, -1, 0, 0)
ans = 0
flag = False
while q:
    cnt, x, y, z = q.popleft()
    for d in range(6):
        nx = x+dx[d]
        ny = y+dy[d]
        nz = z+dz[d]
        if not(0<=nx<H and 0<=ny<N and 0<=nz<M):
            continue
        if arr[nx][ny][nz]==0:
            arr[nx][ny][nz] = 1
            tomato -= 1
            q.append((cnt+1, nx, ny, nz))
            if tomato==0:
                ans = cnt+1
                flag  =True
                break
    if flag : break

if tomato ==0:
    print(ans)
else :
    print(-1)