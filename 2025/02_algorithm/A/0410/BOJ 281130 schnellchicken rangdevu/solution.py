from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]=='A':
            hx, hy = i, j
            arr[i][j]='.'
        elif arr[i][j]=='B':
            wx, wy = i, j
            arr[i][j]='.'

visited = [[0]*M for _ in range(N)]

if wy==0:
    if wx==0: wd=1
    else: wd=0
elif wx==N-1: wd=3
elif wy==M-1: wd=2
elif wx == 0: wd = 1
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

cnt = 0
while arr[wx][wy]=='.':
    arr[wx][wy]=cnt
    cnt+=1
    dx, dy = dxdy[wd]
    nwx, nwy = wx+dx, wy+dy
    if not(0<=nwx<N and 0<=nwy<M):
        wd = (wd+1)%4
        dx, dy = dxdy[wd]
        nwx, nwy = wx + dx, wy + dy

    wx, wy = nwx, nwy

q = deque([(hx, hy, 0, 1)])
visited[hx][hy]=1
ans = -1
while q:
    x, y, t, go = q.popleft()
    if x==0 or x==N-1 or y==0 or y==M-1:
        if t%2 == arr[x][y]%2:
            tmpans = arr[x][y]
            while tmpans<t:
                tmpans += cnt
            if ans==-1: ans = tmpans
            else: ans = min(ans, tmpans)

    cango = 4*go
    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M) or arr[nx][ny]=='G':
            cango -= 1
            continue
        if visited[nx][ny]: continue
        visited[nx][ny]=1
        q.append((nx, ny, t+1, 1))
    if not cango:
        q.append((x, y, t+1, 0))
print(ans)
