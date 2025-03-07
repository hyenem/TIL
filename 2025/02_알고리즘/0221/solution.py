from collections import deque

dxdy = ((1, 0), (-1, 0), (0, 1), (0, -1))
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]: continue
        if arr[i][j]==1: continue
        visited[i][j]=True
        ans += 1
        q = deque()
        q.append((i,j))
        while q:
            x, y = q.popleft()
            for dx, dy in dxdy:
                # 끝과 끝이 연결되어있으므로 다음 칸을 범위 바깥도 봐야함.
                nx, ny = (x+dx)%N, (y+dy)%M
                if visited[nx][ny]: continue
                if arr[nx][ny]==1: continue
                visited[nx][ny]=True
                q.append((nx, ny))
print(ans)
