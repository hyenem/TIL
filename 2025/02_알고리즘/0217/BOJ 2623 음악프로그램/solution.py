from collections import deque

N, M = map(int, input().split())

indegree=[0]*(N+1)
adj = [[] for _ in range(N+1)]
for _ in range(M):
    K, *tmp = map(int, input().split())
    for i in range(1, K):
        adj[tmp[i-1]].append(tmp[i])
        indegree[tmp[i]]+=1

q = deque()
for i in range(1, N+1):
    if indegree[i]==0:
        q.append(i)

ans = []
while q:
    item = q.popleft()
    ans.append(item)
    for ele in adj[item]:
        indegree[ele]-=1
        if indegree[ele]==0:
            q.append(ele)

if len(ans)!=N:
    print(0)
else :
    for ele in ans:
        print(ele)
