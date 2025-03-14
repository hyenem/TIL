def btk(x, y, d, k, cnt):
    global ans
    if cnt>=ans: return

    nd = tile_inout[arr[x][y]][d]
    nx, ny = x+dxdy[nd][0], y+dxdy[nd][1]
    if nx == N - 1 and ny == N:
        ans = min(ans, cnt+1)
        return
    if (0<=nx<N and 0<=ny<N) and not visited[nx][ny] and arr[nx][ny] in goin[nd]:
        visited[nx][ny]=1
        btk(nx, ny, nd, k, cnt+1)
        visited[nx][ny]=0

    if k!=0:
        for i in range(N):
            for j in range(N):
                if visited[i][j]: continue
                if arr[i][j] not in goin[d]: continue
                arr[i][j], arr[x][y] = arr[x][y], arr[i][j]
                nd = tile_inout[arr[x][y]][d]
                nx, ny = x + dxdy[nd][0], y + dxdy[nd][1]
                if nx==N-1 and ny==N:
                    ans = min(ans, cnt+1)
                    return
                if (0<=nx<N and 0<=ny<N) and not visited[nx][ny] and arr[nx][ny] in goin[nd]:
                    visited[nx][ny] = 1
                    btk(nx, ny, nd, k-1, cnt+1)
                    visited[nx][ny] = 0
                arr[i][j], arr[x][y] = arr[x][y], arr[i][j]



N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
goin = ((0, 1, 4), (1, 3, 5), (2, 3, 4), (0, 2, 5))
tile_inout = ((1, -1, -1, 2), (3, 2, -1, -1), (-1, -1, 1, 0),(-1, 0, 3, -1), (0, -1, 2, -1), (-1, 1, -1, 3))

ans = 2501
visited = [[0]*N for _ in range(N)]
btk(0, 0, 1, K, 0)

if ans==2501: ans = -1
print(ans)
