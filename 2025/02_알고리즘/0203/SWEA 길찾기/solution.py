def dfs(c):
    global ans
    if c==99:
        ans = 1
    if ans ==1:
        return
    visited[c]=True
    for ele in adj[c]:
        if not visited[ele]:
            dfs(ele)


for _ in range(1, 11):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(100)]
    for i in range(E):
        adj[arr[i*2]].append(arr[i*2+1])

    visited = [False]*(100)
    ans = 0
    dfs(0)
    print(f'#{tc} {ans}')