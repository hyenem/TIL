from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
q = deque([(0,0,0)])

while q:
    c, x, y = q.popleft()
    if (x, y)==(N-1, N-1):
        ans = c
        break
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x+dx, y+dy
        if not (0<=nx<N and 0<=ny<N): continue
        if visited[nx][ny]: continue
        visited[nx][ny]=True
        if arr[nx][ny]==0:
            q.append((c+1, nx, ny))
        else :
            q.appendleft((c, nx, ny))
print(ans)