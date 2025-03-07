import heapq

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

q = []
for i in range(N):
    visited[i][0]=1
    visited[i][M-1]=1
    heapq.heappush(q, (arr[i][0], i, 0))
    heapq.heappush(q, (arr[i][M-1], i, M-1))
for j in range(M):
    visited[0][j]=1
    visited[N-1][j]=1
    heapq.heappush(q, (arr[0][j], 0, j))
    heapq.heappush(q, (arr[N-1][j], N-1, j))

ans = 0
height = 0
while q:
    h, x, y = heapq.heappop(q)
    height=max(height, h)
    for dx, dy in ((0,1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M): continue
        if visited[nx][ny]: continue
        if height>arr[nx][ny]:
            ans += height-arr[nx][ny]
        visited[nx][ny]=1
        heapq.heappush(q, (arr[nx][ny], nx, ny))

print(ans)