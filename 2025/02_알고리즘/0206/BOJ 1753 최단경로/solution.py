import heapq

V, E = map(int, input().split())
s = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

ans = [-1]*(V+1)
ans[s]=0
q = [(0,s)]
while q:
    weight, node = heapq.heappop(q)
    for ele in adj[node]:
        if ans[ele[1]]==-1 or ans[ele[1]]>weight+ele[0]:
            ans[ele[1]]=weight+ele[0]
            heapq.heappush(q, (weight+ele[0], ele[1]))

for i in range(1, V+1):
    if ans[i]==-1:
        print('INF')
    else :
        print(ans[i])