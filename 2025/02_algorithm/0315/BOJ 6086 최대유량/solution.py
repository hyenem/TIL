import heapq

N = int(input())
adj = {}
for _ in range(N):
    v1, v2, c = input().split()
    c = int(c)
    if v1 not in adj: adj[v1]=[]
    if v2 not in adj : adj[v2]=[]
    adj[v1].append((v2, c))
    adj[v2].append((v1, c))

limit = {}
limit['A']=1000
acc = {}

q = [(1000, 'A')]
rvisited = set()
ans = 0
while q:
    print(q)
    w, v = heapq.heappop(q)

    nw = min(w, rvisited)
    rvisited.add(v)

    for nv, nc in adj[v]:
        if nv in rvisited: continue
        if nv not in limit: limit[nv]=0
        nw = min(w, nc)
        limit[nv]+=nc

        heapq.heappush(q, (nw, nv))

print(w)


# 내가 필요한건 지금까지의 최솟값
# 다 합치고, 그다음에 최솟값 찾는거야