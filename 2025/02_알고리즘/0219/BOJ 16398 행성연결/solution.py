# 프림 알고리즘
# 1000*1000의 edge를 정렬하는게 너무 비효율적으로 느껴짐
import heapq

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

q = [(0,0)]
visited = [False]*N
cost = [-1]*N
cost[0]=0

ans = 0
cnt= 0
while q:
    c, v = heapq.heappop(q)
    if visited[v]: continue
    ans += c
    cnt+=1
    visited[v]=True
    if cnt==N: break

    for i in range(0, N):
        if i==v: continue
        if cost[i]==-1 or cost[i]>adj[v][i]:
            heapq.heappush(q, (adj[v][i], i))

print(ans)