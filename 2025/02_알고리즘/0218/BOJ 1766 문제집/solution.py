import heapq

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
indgree=[0]*(N+1)
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    indgree[v2]+=1

q=[]
for i in range(1, N+1):
    if indgree[i]==0:
        heapq.heappush(q, i)
ans = []
while q:
    item = heapq.heappop(q)
    ans.append(item)
    for ele in adj[item]:
        indgree[ele]-=1
        if indgree[ele]==0:
            heapq.heappush(q, ele)
print(*ans)