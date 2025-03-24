def match(i):
    for w in adj[i]:
        if visited[w]: continue
        visited[w]=1
        if not who[w] or match(who[w]):
            who[w]=i
            return True
    return False

N, M = map(int, input().split())
adj = [[]]
for i in range(N):
    n, *lst = map(int, input().split())
    adj.append(lst)

who = [0]*(M+1)
ans = 0
for i in range(1,N+1):
    visited = [0]*(M+1)
    if match(i): ans += 1

print(ans)