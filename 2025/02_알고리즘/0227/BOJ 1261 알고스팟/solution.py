from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
q = deque()
q.append((0,0,0))
while q:
    c, x, y = q.popleft()
    if x==N-1 and y==M-1:
        print(c)
        break
    for dx, dy in((1,0), (-1, 0), (0, 1), (0,-1)):
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M): continue
        if visited[nx][ny]:continue
        visited[nx][ny]=1
        if arr[nx][ny]==0:
            q.appendleft((c, nx, ny))
        else :
            q.append((c+1, nx, ny))
