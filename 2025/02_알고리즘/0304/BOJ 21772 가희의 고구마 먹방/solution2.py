def btk(x, y, t, cnt):
    global ans
    if t==T:
        ans = max(ans, cnt)
        return
    if cnt+T-t<ans:
        ans = max(ans, cnt)
        return
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x+dx, y+dy
        if not (0<=nx<N and 0<=ny<M): continue
        if visited[nx][ny]: continue
        if arr[nx][ny]=='#': continue
        if arr[nx][ny]=='S':
            visited[nx][ny]=1
            btk(nx, ny, t+1, cnt+1)
            visited[nx][ny]=0
        else :
            btk(nx, ny, t+1, cnt)


N, M, T = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]=='G':
            btk(i, j, 0, 0)
            break
print(ans)