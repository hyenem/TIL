from collections import deque

N = int(input())
adj = {}
edge = []
for _ in range(N):
    v1, v2, c = input().split()
    c = int(c)
    if v1 not in adj: adj[v1]=[]
    if v2 not in adj: adj[v2]=[]
    adj[v1].append([v2, len(edge)])
    adj[v2].append([v1, len(edge)])
    edge.append(c)

ans = 0
while True:
    q = deque([('A', 700_001)])
    visited = {'A'}
    parent = {}
    while q:
        v, c = q.popleft()
        if v=='Z':
            ans += c
            while v in parent:
                v, i = parent[v]
                edge[i]-=c
            break
        for nv, ni in adj[v]:
            nc = edge[ni]
            if nc <= 0: continue
            if nv not in visited:
                visited.add(nv)
                parent[nv]=(v, ni)
                q.append((nv, min(c, nc)))
    else :
        break
print(ans)
