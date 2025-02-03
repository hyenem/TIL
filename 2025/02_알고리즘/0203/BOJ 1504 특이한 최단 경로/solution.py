import heapq
def find(v1, v2):
    visited = [-1]*(V+1)
    q = [(0, v1)]
    visited[v1]=0
    ans = -800000
    while q:
        item = heapq.heappop(q)
        if item[1]==v2:
            ans = item[0]
            break
        for ele in adj[item[1]]:
            if visited[ele[0]]==-1 or visited[ele[0]]>item[0]+ele[1]:
                visited[ele[0]]=item[0]+ele[1]
                heapq.heappush(q, (item[0]+ele[1], ele[0]))
    return ans


V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, c = map(int, input().split())
    adj[s].append((e,c))
    adj[e].append((s,c))

v1, v2 = map(int, input().split())
ans1 = find(1, v1)+find(v1,v2)+find(v2,V)
ans2 = find(1, v2)+find(v1,v2)+find(v1,V)
if ans1<0:
    if ans2<0:
        print(-1)
    else :
        print(ans2)
elif ans2<0:
    print(ans1)
else :
    print(min(ans1, ans2))