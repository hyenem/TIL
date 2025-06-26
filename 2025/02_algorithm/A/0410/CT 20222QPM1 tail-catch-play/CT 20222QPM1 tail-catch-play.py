from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dxdy = ((0, 1), (-1, 0), (0, -1), (1, 0))
for round in range(K):
    round = round%(4*N)
    tmp = [ele[:] for ele in arr]
    for i in range(N):
        for j in range(N):
            if tmp[i][j]==3:
                arr[i][j]=4
                for dx, dy in dxdy:
                    nx, ny = i+dx, j+dy
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny]==2:
                        arr[nx][ny]=3
    for i in range(N):
        for j in range(N):
            if tmp[i][j]==1:
                arr[i][j]=2
                for dx, dy in dxdy:
                    nx, ny = i+dx, j+dy
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny]==4:
                        arr[nx][ny]=1

    sd = round//N
    sx, sy = ((round%N, -1), (N, round%N), (N-1-round%N, N), (-1, N-1-round%N))[sd]
    dx, dy = dxdy[sd]
    while 0<=sx+dx<N and 0<=sy+dy<N:
        sx, sy = sx+dx, sy+dy
        if arr[sx][sy] in {1, 2, 3}:
            q = deque([(sx, sy, 1)])
            visited = [[0]*N for _ in range(N)]
            visited[sx][sy]=1
            ht = []
            while q:
                x, y, cnt = q.popleft()

                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<N and 0<=ny<N): continue
                    if visited[nx][ny]: continue
                    if arr[x][y]==3:
                        if arr[nx][ny]==2:
                            visited[nx][ny] = 1
                            q.append((nx, ny, cnt + 1))
                    else:
                        if arr[nx][ny] in {1,2,3}:
                            visited[nx][ny]=1
                            q.append((nx, ny, cnt+1))
                if arr[x][y]==1:
                    arr[x][y]=3
                    ans += cnt**2

                elif arr[x][y]==3:
                    arr[x][y]=1

            break

print(ans)