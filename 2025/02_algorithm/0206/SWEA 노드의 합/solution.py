def post(idx):
    if 2*idx<=N:
        tree[idx]+=post(2*idx)
    if 2*idx+1<=N:
        tree[idx]+=post(2*idx+1)
    return tree[idx]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree= [0]*(N+1)
    for _ in range(M):
        n, d = map(int, input().split())
        tree[n]=d
    post(1)

    print(f'#{tc} {tree[L]}')