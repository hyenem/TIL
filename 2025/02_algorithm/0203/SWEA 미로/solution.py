def dfs(x, y):
    global ans
    if ans ==1 :
        return
    visited[x][y]=True
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<N:
            if (nx, ny) == end:
                ans = 1
                return
            if not visited[nx][ny]:
                dfs(nx, ny)


T = int(input())
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
for tc in range(1, T+1):
    N = int(input())
    arr = []
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        data = list(map(int,input()))
        arr.append(data)
        for j in range(N):
            if data[j]==2:
                start = (i, j)
            elif data[j]==3:
                end = (i, j)
            elif data[j]==1:
                visited[i][j]=True
    ans = 0
    dfs(start[0], start[1])
    print(f'#{tc} {ans}')