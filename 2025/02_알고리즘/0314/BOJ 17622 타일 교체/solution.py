def go():
    global ans, d, x, y
    print(x, y)
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    while True:
        cnt+=1
        if ans!=-1 and cnt>=ans: return

        dx, dy = dxdy[d]
        nx, ny = x + dx, y + dy
        print(nx, ny)
        if nx == N and ny == N - 1:
            ans = cnt
            return

        if not (0 <= nx < N and 0 <= ny < N): return
        if visited[nx][ny]: return
        if tile_inout[arr[nx][ny]][d] == -1: return

        visited[nx][ny] = 1
        x, y = nx, ny
        d = tile_inout[arr[nx][ny]][d]

N, K = map(int, input().split())
x, y, d = 0, -1, 1
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
tile_inout = ((1, -1, -1, 2), (3, 2, -1, -1), (-1, -1, 1, 0),(-1, 0, 3, -1), (0, -1, 2, -1), (-1, 1, -1, 3))

ans = -1
if K==0:
    go()
    print(ans)
else :
    for i in range(N*N):
        for j in range(i+1, N*N):
            x1, y1 = i//N, i%N
            x2, y2 = j//N, j%N
            arr[x1][y1], arr[x2][y2] = arr[x2][y2], arr[x1][y1]
            go()
            arr[x1][y1], arr[x2][y2] = arr[x2][y2], arr[x1][y1]
    print(ans)