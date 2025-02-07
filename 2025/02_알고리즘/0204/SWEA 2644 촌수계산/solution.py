V = int(input())
S, G = map(int, input().split())
E = int(input())
adj = [[] for _ in range(V+1)]
visited = [False]*(V+1)
for _ in range(E):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

# q에 촌수와 사람 번호를 저장
q = [(0, S)]
visited[S]=True
ans = -1
while q:
    cnt, num = q.pop(0)
    if num==G:
        ans = cnt
        break
    for ele in adj[num]:
        if not visited[ele]:
            visited[ele]=True
            q.append((cnt+1, ele))
print(ans)