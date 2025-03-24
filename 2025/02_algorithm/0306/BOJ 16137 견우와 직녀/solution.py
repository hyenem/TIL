import heapq

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = ((1, 0), (-1, 0), (0, 1), (0, -1))
candidate = []
for i in range(N):
    for j in range(N):
        if arr[i][j]==0:
            if i == 0:
                arr[1][j]==1
                candidate.append((i,j))
                continue
            elif i==N-1:
                arr[N-2][j]==1
                candidate.append((i,j))
                continue
            else:
                if arr[i-1][j]==arr[i+1][j]==1:
                    candidate.append((i,j))
                    continue

            if j == 0:
                arr[i][1]==1
                candidate.append((i,j))
                continue
            elif j==N-1:
                arr[i][N-2]==1
                candidate.append((i,j))
                continue
            else:
                if arr[i][j-1]==arr[i][j+1]==1:
                    candidate.append((i,j))
                    continue

ans = 2001
for cx, cy in candidate:
    if ans==2*(N-1): break
    arr[cx][cy]=K
    visited = [[-1]*N for _ in range(N)]
    q = [(0, 0, 0)]
    visited[0][0]=0
    while q:
        t, x, y = heapq.heappop(q)
        if x==y==N-1:
            ans = min(ans, t)
            break

        if visited[x][y]!=-1 and t>visited[x][y]: continue
        for dx, dy in dxdy:
            nx, ny = x+dx, y+dy
            if not (0<=nx<N and 0<=ny<N): continue
            if arr[nx][ny]==0: continue
            if arr[x][y]!=1 and arr[nx][ny]!=1: continue
            nt = (t//arr[nx][ny]+1)*arr[nx][ny]
            if visited[nx][ny]==-1 or visited[nx][ny]>nt:
                visited[nx][ny]=nt
                heapq.heappush(q, (nt, nx, ny))

    arr[cx][cy]=0

print(ans)

