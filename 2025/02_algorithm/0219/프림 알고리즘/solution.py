import heapq

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, c = map(int, input().split())
        adj[s].append((c, e))
        adj[e].append((c, s))

    q = [(0,0)]
    cost = [-1] * (V+1)
    cost[0]=0
    visited = [False]*(V+1)
    ans = 0
    while q:
        c, v = heapq.heappop(q)
        if visited[v]:continue
        visited[v]=True
        ans += c
        for nc, nv in adj[v]:
            if cost[nv]==-1 or cost[nv]>nc:
                cost[nv]=nc
                heapq.heappush(q,(nc, nv))

    print(f'#{tc} {ans}')