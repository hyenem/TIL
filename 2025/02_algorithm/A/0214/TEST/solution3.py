from collections import deque

dxdy = ((1, 0), (-1, 0),(0,-1),(0,1))
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(K)]
    arr = [[0]*(M+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]
    q = deque()
    visited = [[False]*(M+2) for _ in range(N+2)]
    t=0
    for x, y in points:
        if arr[x+1][y+1]!=0:
            q.append((x+1, y+1, 1))
            visited[x+1][y+1]=True
    while q:
        x, y, t = q.popleft()
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if visited[nx][ny]: continue
            if arr[nx][ny]==1:
                visited[nx][ny]=True
                q.append((nx, ny, t+1))

    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j]==1 and not visited[i][j]:
                cnt+=1

    print(f'#{tc} {t} {cnt}')
