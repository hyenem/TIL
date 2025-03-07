# 크루스칼 알고리즘

def lenth(s):
    if s=='0':
        return -1
    elif 0<=ord(s)-ord('a')<26:
        return ord(s)-ord('a')+1
    else :
        return ord(s)-ord('A')+27
def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

N = int(input())
edge = []
ans = 0
for i in range(N):
    tmp = list(input())
    for j in range(N):
        l = lenth(tmp[j])
        if l==-1 : continue

        ans += l
        if i==j: continue

        edge.append((l, i, j))

p = [i for i in range(N)]
r = [0]*N
edge.sort()
cnt = 0
for l, x, y in edge:
    px, py = find(x), find(y)
    if px==py: continue
    ans -= l
    cnt+=1
    if cnt==N-1:
        break

    #union
    if r[px]<r[py]:
        p[px]=py
    else :
        p[py]=px
        if r[px]==r[py]: r[px]+=1

if cnt!=N-1:
    print(-1)
else :
    print(ans)