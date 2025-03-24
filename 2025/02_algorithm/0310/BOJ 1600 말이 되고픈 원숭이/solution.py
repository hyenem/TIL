from collections import deque

K = int(input())
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
hdxdy = ((1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
dxdy = ((0,1), (0, -1), (-1, 0), (1, 0))
visited = [[-1]*M for _ in range(N)]
q = deque([(0,K, 0, 0)])
visited[0][0]=0
while q:
    t, k, x, y = q.popleft()

    if x==N-1 and y==M-1:
        print(t)
        break

    for dx, dy in dxdy:
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M): continue
        if arr[nx][ny]: continue
        if visited[nx][ny]==-1 or visited[nx][ny]<k:
            visited[nx][ny]=k
            q.append((t+1, k, nx, ny))

    if k==0: continue
    for dx, dy in hdxdy:
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M): continue
        if arr[nx][ny]: continue
        if visited[nx][ny]==-1 or visited[nx][ny]<k-1:
            visited[nx][ny]=k-1
            q.append((t+1, k-1, nx, ny))
else :
    print(-1)