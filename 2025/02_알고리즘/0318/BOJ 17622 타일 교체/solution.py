def btk(x, y, ind, cnt, canchange):
    global ans
    if cnt>=ans: return
    for tile , outd in cango[ind]:
        if tile==arr[x][y]:
            dx, dy = dxdy[outd]
            nx, ny = x+dx, y+dy
            if nx==N-1 and ny==N and cnt+canchange<=N*N:
                ans = min(ans, cnt)
                return
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny]=1
                btk(nx, ny, outd, cnt+1, canchange)
                visited[nx][ny]=0
            break

    if canchange:
        for tile, outd in cango[ind]:
            if tile==arr[x][y]: continue
            dx, dy = dxdy[outd]
            nx, ny = x+dx, y+dy
            if nx==N-1 and ny==N:
                ans = min(ans, cnt)
                return
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny]=1
                btk(nx, ny, outd, cnt+1, canchange-1)
                visited[nx][ny]=0

N, K = map(int, input().split())
cango = (((0, 1), (1, 3), (4, 0)), ((1, 2), (3, 0), (5, 1)), ((2, 1), (3, 3), (4, 2)), ((0, 2), (2, 0), (5, 3)))
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
ans = N*N+1
btk(0, 0, 1, 1, K)

if ans==N*N+1: ans = -1
print(ans)