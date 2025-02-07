def post(idx):
    # 리프노드인 경우 숫자만 리턴
    if len(tree[idx])==1:
        return tree[idx][0]
    # 그 외의 경우 양쪽 계산해서 리턴
    else:
        left = post(tree[idx][1])
        right = post(tree[idx][2])
        if tree[idx][0]=='+':
            return left+right
        elif tree[idx][0]=='-':
            return left-right
        elif tree[idx][0]=='*':
            return left*right
        elif tree[idx][0]=='/':
            return left/right

for tc in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)
    for _ in range(N):
        idx, *data = input().split()
        if len(data)==3:
            data[1] = int(data[1])
            data[2] = int(data[2])
        else :
            data[0] = int(data[0])
        tree[int(idx)]=data
    print(f'#{tc} {int(post(1))}')
