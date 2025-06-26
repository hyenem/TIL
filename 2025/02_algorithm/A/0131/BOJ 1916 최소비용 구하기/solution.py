import heapq

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    adj[s].append((e,c))
start, end = map(int, input().split())

min = [-1]*(N+1)
q = []
heapq.heappush(q, (0, start))
min[start] = 0
while q:
    p, t = heapq.heappop(q)
    if t==end:
        ans = p
        break
    for next in adj[t]:
        if min[next[0]]==-1 or min[next[0]]>p+next[1]:
            min[next[0]]=p+next[1]
            heapq.heappush(q, (p+next[1], next[0]))
print(ans)