import heapq

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V)]
    for _ in range(E):
        s, e, c = map(int, input().split())
        adj[s].append((c,e))

    q = []
    heapq.heappush(q, (0,0))
    visited = [50000]*V
    visited[0]=0
    ans = 0
    while q:
        c, node = heapq.heappop(q)
        if node ==V-1:
            ans = c
            break
        for dc, next in adj[node]:
            if dc+c<visited[next]:
                heapq.heappush(q, (c+dc, next))
    print(f'#{tc} {ans}')