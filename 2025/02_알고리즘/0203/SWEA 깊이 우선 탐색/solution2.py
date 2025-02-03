def dfs(c):
    visited[c]=True
    ans.append(c)
    for ele in adj[c]:
        if not visited[ele]:
            dfs(ele)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    for row in adj:
        row.sort()

    visited = [False]*(V+1)
    ans = []
    dfs(1)

    print(f'#{tc}', *ans)