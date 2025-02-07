T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    s, g = map(int, input().split())

    visited = [False]*(V+1)
    # q에는 출발점에서 해당 점까지의 거리와 점이 저장된다
    q = [(0,s)]
    visited[s]=True
    ans = 0
    while q:
        cost, node = q.pop(0)
        if node == g:
            ans = cost
            break
        for ele in adj[node]:
            if not visited[ele]:
                q.append((cost+1, ele))
                visited[ele]=True
    print(f'#{tc} {ans}')
