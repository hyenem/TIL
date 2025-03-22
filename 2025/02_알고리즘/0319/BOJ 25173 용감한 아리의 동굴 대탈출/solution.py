from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

ax = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            ax, ay = i, j
            for d in range(4):
                dx, dy = dxdy[d]
                nx, ny = ax + dx, ay + dy
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 3:
                    bx, by = nx, ny
                    bd = (d + 2) % 4
                    ad = (d + 2) % 4
                    break
            break
    if ax: break

ah, aa, bh, ba = map(int, input().split())

while True:
    bh -= aa
    if bh <= 0:
        print('VICTORY!')
        break

    bax, bay, bad = ax, ay, ad

    for k in range(4):
        dx, dy = dxdy[ad]
        nx, ny = ax + dx, ay + dy
        if 0 <= nx < N and 0 <= ny < M and (nx, ny) != (bx, by) and arr[nx][ny] != 1:
            ax, ay = nx, ny
            break
        ah -= 1
        ad = (ad + 1) % 4

    if ah <= 0:
        print("CAVELIFE...")
        break

    cnt = 1
    nbd = bd
    nbx, nby = bx, by
    babyx, babyy = -1, -1
    l = 1
    while cnt < N * M:
        l += 1
        dx, dy = dxdy[nbd]
        for _ in range(l // 2):
            nbx, nby = nbx + dx, nby + dy
            if 0 <= nbx < N and 0 <= nby < M:
                cnt += 1
                if arr[nbx][nby] == 1:
                    babyx, babyy = nbx, nby
                    break
        if babyx != -1:
            break
        nbd = (nbd + 1) % 4
    else:
        if (bax, bay) == (ax, ay): continue
        bx, by, bd = bax, bay, ad
        continue

    q = deque([(ba, babyx, babyy)])
    visited = [[0] * M for _ in range(N)]
    visited[babyx][babyy] = 1
    while q:
        h, x, y = q.popleft()
        if h == 0: break
        if x == ax and y == ay:
            ah -= h
            break

        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] != 1 and (nx, ny) != (bx, by):
                visited[nx][ny] = 1
                q.append((h - 1, nx, ny))

    if ah <= 0:
        print("CAVELIFE...")
        break

    if (bax, bay) == (ax, ay): continue
    bx, by, bd = bax, bay, ad
