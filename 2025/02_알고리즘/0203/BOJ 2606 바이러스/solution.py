def dfs(c):
    global ans
    # 방문할 때마다 1씩 답을 올리기
    ans += 1
    for ele in adj[c]:
        if not visited[ele]:
            # 방문표시하고
            visited[ele]=True
            # dffs 돌기
            dfs(ele)

V = int(input())
E = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)
# 1번 컴퓨터는 답에서 빠지므로 -1로 시작
ans = -1
visited = [False]*(V+1)
visited[1] = True
dfs(1)
print(ans)