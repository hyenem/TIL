def dfs(c):
    global end, ans
    visited[c] = True
    if c==end:
        ans = 1
    if ans ==1:
        return
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

    start, end = map(int, input().split())
    # 시작점을 stack에 넣어둠
    visited = [False]*(V+1)
    ans = 0
    print(f'#{tc} {ans}')
