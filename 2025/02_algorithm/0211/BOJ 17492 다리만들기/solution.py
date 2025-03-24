import heapq
from collections import deque

dxdy = ((-1, 0), (1, 0), (0, 1), (0,-1))
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lvisited = [[False]*M for _ in range(N)]
land = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==1 and not lvisited[i][j]:
            q = deque()
            land.append([(i, j)])
            q.append((i, j))
            arr[i][j]=len(land)
            while q:
                x, y = q.popleft()
                for dx, dy in dxdy:
                    nx, ny = x+dx, y+dy
                    if not(0<=nx<N and 0<=ny<M): continue
                    if arr[nx][ny]==1 and not lvisited[nx][ny]:
                        lvisited[nx][ny]=True
                        land[-1].append((nx, ny))
                        q.append((nx, ny))
                        arr[nx][ny]=arr[x][y]
K = len(land)
adj = [[] for _ in range(K)]
for i in range(K):
    for point in land[i]:
        for dx, dy in dxdy:
            x, y = point
            lenth = 0
            while True:
                x+=dx
                y+=dy
                lenth+=1
                if not(0<=x<N and 0<=y<M):break
                if arr[x][y]==0:
                    continue
                else:
                    if lenth>=3:
                        adj[i].append((lenth-1, arr[x][y]-1))
                    break

hq = []
heapq.heappush(hq, (0, 0))
visited = [600]*K
visited[0]=0
tvisited = [False]*K
cnt=0
ans = 0
while hq:
    c, l = heapq.heappop(hq)
    if not tvisited[l]:
        tvisited[l] = True
        cnt+=1
        ans += c
    else : continue
    if cnt==K:
        break
    for nc, nl in adj[l]:
        if visited[nl]>nc:
            visited[nl]=nc
            heapq.heappush(hq, (nc, nl))
if cnt==K:
    print(ans)
else :
    print(-1)