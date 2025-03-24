def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if px==py: return

    # 내가 하나짜리면 나를 밑으로 붙이기
    if px==x:
        parent[px]=py
    # 내가 하나짜리가 쟤를 내 밑으로 붙이기
    else :
        parent[py]=px

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # makeset
    parent = [i for i in range(N+1)]

    arr = list(map(int, input().split()))
    for i in range(M):
        p1, p2 = arr[2*i], arr[2*i+1]
        union(p1, p2)

    for i in range(1, N+1):
        find(i)
    print(f'#{tc} {len(set(parent))-1}')