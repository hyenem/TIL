def inord(idx):
    if len(tree[idx])>=2:
        inord(tree[idx][1])
    print(tree[idx][0], end='')
    if len(tree[idx])>=3:
        inord(tree[idx][2])

for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for _ in range(N):
        data = list(input().split())
        tree[int(data[0])] = [data[1]]
        for ele in data[2:]:
            tree[int(data[0])].append(int(ele))
    print(f'#{tc}', end=' ')
    inord(1)
    print()