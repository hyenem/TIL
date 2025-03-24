# 시간 비교해보고싶어서
# cnt(V-1) 적용해보았습니다.

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    px = find(x)
    py = find(y)
    p[px] = py


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge = []
    cnt = 0
    ans = 0
    for _ in range(E):
        s, e, c = map(int, input().split())
        edge.append((c, s, e))
    edge.sort()

    p = [i for i in range(V + 1)]
    idx = 0
    while cnt < V:
        c, s, e = edge[idx]
        idx += 1
        if find(s) == find(e): continue
        ans += c
        cnt += 1
        union(s, e)

    print(f'#{tc} {ans}')