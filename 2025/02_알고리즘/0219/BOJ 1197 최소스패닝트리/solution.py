def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

V, E = map(int, input().split())

edge = []
for i in range(E):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))
edge.sort()

cnt = 0
ans = 0
p = [i for i in range(V+1)]
rank = [0]*(V+1)
for c, a, b in edge:
    pa, pb = find(a), find(b)
    if pa==pb:
        continue

    #union
    if rank[pa]<rank[pb]:
        p[pa]=pb
    else :
        p[pb]=pa
        if rank[pa]==rank[pb]:
            rank[pa]+=1
    ans += c
    cnt+=1
    if cnt==V-1: break
print(ans)