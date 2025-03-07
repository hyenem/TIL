import heapq

N = int(input())
q = []
cnt = 0
cost = [-1]*N
visited = [False]*N
for i in range(N):
    heapq.heappush(q, (int(input()), i))

ans = 0
arr = [list(map(int, input().split())) for _ in range(N)]
while q:
    c, n = heapq.heappop(q)
    if visited[n]: continue
    ans+=c
    visited[n]=True
    cnt+=1
    if cnt==N: break
    for i in range(N):
        if i==n: continue
        if cost[i]==-1 or arr[n][i]<cost[i]:
            cost[i]=arr[n][i]
            heapq.heappush(q, (cost[i], i))
print(ans)