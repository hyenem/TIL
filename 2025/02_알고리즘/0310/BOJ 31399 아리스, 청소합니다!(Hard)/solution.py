N, M = map(int, input().split())
x, y, d = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
warp = [[[0 for _ in range(4)] for _ in range(M)] for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

ans = 0
time = 0
acctime = 0
stack = []
while True:
    time += 1
    if visited[x][y]:
        if stack and (x, y, d) == (stack[0][0], stack[0][1], stack[0][2]):
            break
        stack.append((x, y, d, time))

        if warp[x][y][d]:
            x, y, d, at = warp[x][y][d]
            time += at

        d = (d+B[x][y])%4
    else :
        visited[x][y]=1
        while stack:
            wx, wy, wd, at = stack.pop()
            warp[wx][wy][wd]=(x, y, d, time-at)

        ans = time
        d = (d+A[x][y])%4

    x += dxdy[d][0]
    y += dxdy[d][1]
    if not (0<=x<N and 0<=y<M):
        break

print(ans)