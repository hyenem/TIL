# !!! 문제 꼼꼼히 읽을것!!!
# 번호가 작은 정점부터 방문
def dfs(s):
    for ele in sorted(adj[s]):
        if not visited[ele]:
            ans_dfs.append(ele)
            visited[ele]=True
            dfs(ele)

V, E, S = map(int, input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

visited = [False]*(V+1)
ans_dfs=[S]
# dfs는 재귀로 구현
visited[S]=True
dfs(S)

# bfs는 list와 포인터로 구현
# (queue와 정답 배열을 따로 만들지 않기 위함임)
ans_bfs=[S]
head = 0
visited = [False]*(V+1)
visited[S]=True
while len(ans_bfs)!=head:
    #pop
    item = ans_bfs[head]
    head += 1
    for ele in sorted(adj[item]):
        if not visited[ele]:
            visited[ele]=True
            ans_bfs.append(ele)

print(*ans_dfs)
print(*ans_bfs)