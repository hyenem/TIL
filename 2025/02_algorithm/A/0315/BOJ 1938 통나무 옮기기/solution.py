from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]
dxdy = ((0, 1),(1, 0), (-1, 0), (0, -1))
edxdy = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
ex, ey = -1, -1
for i in range(N):
    for j in range(N):
        if arr[i][j]=='B':
            if i!=N-1 and arr[i+1][j]=='B':
                cx, cy, d = i+1, j, 1
                arr[i][j], arr[i+1][j], arr[i+2][j]=0, 0, 0
            elif arr[i][j+1]=='B':
                cx, cy, d = i, j+1, 0
                arr[i][j], arr[i][j+1], arr[i][j+2]=0, 0, 0
        elif arr[i][j]=='E':
            if ex==-1:
                if i!=N-1 and arr[i+1][j]=='E':
                    ex, ey = i+1, j
                elif arr[i][j+1]=='E':
                    ex, ey = i, j+1
        else : arr[i][j]=int(arr[i][j])

visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
q = deque([(0, cx, cy, d)])
visited[cx][cy][d]=1

while q:
    cnt, x, y, d = q.popleft()

    dx, dy = dxdy[d]
    if not (0 <= x+dx < N and 0 <= y+dy < N) or arr[x+dx][y+dy]==1: continue
    if not (0 <= x-dx < N and 0 <= y-dy < N) or arr[x-dx][y-dy]==1: continue

    if x==ex and y==ey and arr[x+dx][y+dy]=='E':
        print(cnt)
        break

    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if not (0<=nx<N and 0<=ny<N): continue
        if visited[nx][ny][d]: continue
        if arr[nx][ny]==1: continue
        visited[nx][ny][d]=1
        q.append((cnt+1, nx, ny, d))

    if not visited[x][y][1-d]:
        for dx, dy in edxdy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<N) or arr[nx][ny]==1:
                break
        else :
            visited[x][y][1-d]=1
            q.append((cnt+1, x, y, 1-d))

else :
    print(0)