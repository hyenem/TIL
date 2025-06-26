from collections import deque

N, M, K = map(int, input().split())
wall = [list(map(int, input())) for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))

visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]
q = deque([(0, 0, K, 0, 1)])
visited[0][0][0]=K
while q:
    x, y, canbreak, night, cnt = q.popleft()
    if (x, y)==(N-1, M-1):
        print(cnt)
        break

    if visited[x][y][1-night]<canbreak:
        q.append((x, y, canbreak, 1-night, cnt+1))

    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M): continue

        if wall[nx][ny]:
            if canbreak and not night:
                if visited[nx][ny][1-night]>=canbreak-1: continue
                visited[nx][ny][1-night]=canbreak-1
                q.append((nx, ny, canbreak-1, 1-night, cnt+1))
        else:
            if visited[nx][ny][1-night]>=canbreak: continue
            visited[nx][ny][1-night]=canbreak
            q.append((nx, ny, canbreak, 1-night, cnt+1))
else:
    print(-1)

