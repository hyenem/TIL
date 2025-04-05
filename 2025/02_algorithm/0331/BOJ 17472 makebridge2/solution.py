import heapq
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited =[[0]*M for _ in range(N)]
dxdy = ((-1, 0), (0, 1), (1, 0), (0, -1))
idx = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]==0: continue
        if visited[i][j]: continue
        idx += 1

        q = deque([(i, j)])
        arr[i][j]=idx
        visited[i][j]=1
        while q:
            x, y = q.popleft()
            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if not(0<=nx<N and 0<=ny<M) or visited[nx][ny]: continue
                if arr[nx][ny]==1:
                    visited[nx][ny]=1
                    arr[nx][ny]=idx
                    q.append((nx, ny))

INF = N*M
adj = [[INF]*(idx+1) for _ in range(idx+1)]
for i in range(N):
    for j in range(M):
        if arr[i][j]==0: continue

        for dx, dy in dxdy:
            nx, ny = i, j
            cnt = -1
            while 0<=nx+dx<N and 0<=ny+dy<M:
                cnt += 1
                nx, ny = nx+dx, ny+dy
                if arr[nx][ny]==0:
                    continue
                elif arr[nx][ny]==arr[i][j]:
                    break
                else:
                    if cnt>1:
                        adj[arr[nx][ny]][arr[i][j]]=min(adj[arr[nx][ny]][arr[i][j]], cnt)
                        adj[arr[i][j]][arr[nx][ny]]=min(adj[arr[i][j]][arr[nx][ny]], cnt)
                    break

visited = [1]
ans = 0
for _ in range(idx-1):
    minimum, minidx = INF, -1
    for v in visited:
        for nv in range(1, idx+1):
            if nv in visited: continue

            if minimum>adj[v][nv]:
                minimum=adj[v][nv]
                minidx=nv

    if minidx==-1:
        print(-1)
        break

    ans += minimum
    visited.append(minidx)
else:
    print(ans)
