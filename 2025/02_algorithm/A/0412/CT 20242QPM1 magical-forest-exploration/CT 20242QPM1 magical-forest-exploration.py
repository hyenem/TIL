from collections import deque

dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
N, M, K = map(int, input().split())
arr = [[0]*M for _ in range(3+N)]
move = ((1, 0, 0, ((1, -1), (2, 0), (1, 1))),
        (1, -1, -1, ((-1, -1), (0, -2), (1, -1), (2, -1), (1, -2))),
        (1, 1, 1, ((-1, 1), (0, 2), (1, 1), (1, 2), (2, 1))))

ans = 0
for idx in range(1, K+1):
    gy, gd = map(int, input().split())
    gx, gy = 1, gy-1

    while True:
        for dx, dy, dd, empty in move:
            for mx, my in empty:
                if not(0<=gx+mx<N+3 and 0<=gy+my<M): break
                if arr[gx+mx][gy+my]: break
            else:
                gx, gy, gd = gx+dx, gy+dy, (gd+dd)%4
                break
        else:
            break

    if gx<4:
        arr = [[0]*M for _ in range(N+3)]
        continue

    arr[gx][gy] = idx
    for d in range(4):
        dx, dy= dxdy[d]
        gnx, gny = gx+dx, gy+dy
        if gd==d:
            arr[gnx][gny]=-idx
        else:
            arr[gnx][gny]=idx

    visited = [[0]*M for _ in range(N+3)]
    q = deque([(gx, gy)])
    visited[gx][gy]=1
    maxx = 0
    while q:
        x, y = q.popleft()
        maxx = max(x, maxx)

        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<N+3 and 0<=ny<M): continue
            if visited[nx][ny]: continue
            if arr[x][y]<0:
                if arr[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx, ny))
            else:
                if abs(arr[nx][ny])==arr[x][y]:
                    visited[nx][ny]=1
                    q.append((nx, ny))
    ans += maxx-2
print(ans)