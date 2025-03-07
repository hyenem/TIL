from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q=deque([(0,0)])
ans = 0
while q:
    x, y = q.popleft()
    if x==N-1 and y==M-1:
        ans += 1
        continue
    for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
        nx, ny = x+dx, y+dy
        if not (0<=nx<N and 0<=ny<M): continue
        if arr[nx][ny]<arr[x][y]:
            q.append((nx, ny))
print(ans)