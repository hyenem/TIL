def shoot(i, j, sd):
    global ans

    cnt = 0
    d = sd
    dx, dy = dxdy[d]
    x, y = i+dx, j+dy
    while True:
        if not(0<=x<N and 0<=y<N):
            cnt += 1
            d = (d+2)%4
            dx, dy = dxdy[d]
            x, y = x+dx, y+dy
            continue

        if (x, y)==(i, j) or arr[x][y]==-1: break

        if arr[x][y] >= 6:
            for wx, wy in warm[arr[x][y]]:
                if (wx, wy) != (x, y):
                    x, y = wx, wy
                    break

        if 1<=arr[x][y]<=5:
            cnt += 1
            d = block[arr[x][y]][d]

        dx, dy =dxdy[d]
        x, y = x+dx, y+dy

    ans = max(ans, cnt)



T = int(input())
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
block = (0, (2, 3, 1, 0), (1, 3, 0, 2), (3, 2, 0, 1), (2, 0, 3, 1), (2, 3, 0, 1))
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    warm = {}
    for i in range(N):
        for j in range(N):
            if 6<=arr[i][j]<=10:
                if arr[i][j] not in warm:
                    warm[arr[i][j]] = []
                warm[arr[i][j]].append((i, j))

    ans = 0
    for i in range(N):
        for j in range(N):
            for d in range(4):
                if arr[i][j]!=0: continue
                shoot(i, j, d)
    print(f'#{tc} {ans}')