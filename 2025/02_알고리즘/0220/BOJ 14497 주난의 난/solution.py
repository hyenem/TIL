import heapq

N, M = map(int, input().split())
x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
arr = [list(input()) for _ in range(N)]
arr[x1][y1]=1
arr[x2][y2]=0
dxdy = ((1, 0), (-1,0), (0,-1),(0,1))

q = [(1, x1, y1)]
visited = [[-1]*M for _ in range(N)]

while q:
    t, x, y = heapq.heappop(q)
    if x==x2 and y==y2:
        ans = t
        break
    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if not (0<=nx<N and 0<=ny<M):continue
        if visited[nx][ny]==-1 or visited[nx][ny]>t+int(arr[nx][ny]):
            visited[nx][ny]=t+int(arr[nx][ny])
            heapq.heappush(q, (visited[nx][ny], nx, ny))
print(ans)