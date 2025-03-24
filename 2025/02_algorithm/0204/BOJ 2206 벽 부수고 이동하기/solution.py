from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

ans = -1
q = deque()
q.append((1, 0, 0, False))
broken_visited = [[False]*M for _ in range(N)]
nonbroken_visited = [[False]*M for _ in range(N)]
nonbroken_visited[0][0]=True
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

while q:
    item = deque.popleft(q)
    c, x, y, broken = item
    if (x, y)==(N-1, M-1):
        ans = c
        break
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            if broken and not broken_visited[nx][ny]:
                if arr[nx][ny]==0:
                    broken_visited[nx][ny]=True
                    q.append((c+1, nx, ny, broken))
            elif not broken and not nonbroken_visited[nx][ny]:
                if arr[nx][ny]==0:
                    nonbroken_visited[nx][ny]=True
                    q.append((c+1, nx, ny, broken))
                else :
                    nonbroken_visited[nx][ny] = True
                    q.append((c + 1, nx, ny, True))
print(ans)