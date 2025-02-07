def dfs(node, cnt, visited):
    global ans
    if cnt>=ans:
        return
    for ele in adj[node]:
        if ele==g:
            ans = min(ans, cnt+1)
            return
        if visited&(1<<ele)==0:
            dfs(ele, cnt+1, visited|(1<<ele))

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    s, g = map(int, input().split())

    ans = V+10
    dfs(s, 0, 1<<s)
    if ans==V+10:
        ans = 0
    print(f'#{tc} {ans}')
