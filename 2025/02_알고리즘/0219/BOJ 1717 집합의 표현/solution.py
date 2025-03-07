def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

N, M =  map(int, input().split())

p = [i for i in range(N+1)]
rank = [0]*(N+1)

for _ in range(M):
    f, v1, v2 = map(int, input().split())
    p1 = find(v1)
    p2 = find(v2)
    if f==0:
        #UNION
        if rank[p1]<rank[p2]:
            p[p1]=p2
        else :
            p[p2]=p1
            if rank[p1]==rank[p2]:
                rank[p1]+=1
    else :
        if p1==p2:
            print('YES')
        else :
            print('NO')