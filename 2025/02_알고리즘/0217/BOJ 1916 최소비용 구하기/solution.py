import heapq

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    adj[s].append((c,e))

start, end = map(int, input().split())

q = [(0,start)]
visited = [-1]*(N+1)
visited[start] = 0
ans = 0
while q:
    c, v = heapq.heappop(q)

    # 도착하면 끝내기
    if v==end:
        ans = c
        break

    for dc, nv in adj[v]:
        # 아직 안넣었거나
        # 지금 있는 칸에서 가는게 기존에 저장되어 있던것보다 빠르면 넣기
        if visited[nv]==-1 or visited[nv]>dc+c:
            visited[nv]=dc+c
            heapq.heappush(q, (visited[nv], nv))
print(ans)