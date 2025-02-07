def dfs(x, y, cnt, arr):
    global ans
    if cnt>ans:
        return
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<N:
            if arr[nx][ny]==3:
                ans = min(ans, cnt)
                return
            if arr[nx][ny]==0:
                arr[nx][ny]=1
                dfs(nx, ny, cnt+1, arr)
                arr[nx][ny]=0

T = int(input())
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = N*N+1
    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                x, y = i, j
    dfs(x, y, 0, arr)

    if ans == N*N+1:
        ans = 0
    print(f'#{tc} {ans}')
