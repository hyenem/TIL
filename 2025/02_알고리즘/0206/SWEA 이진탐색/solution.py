def inord(n):
    global cnt
    if 2*n<=N:
        inord(2*n)
    tree[n]=cnt
    cnt+=1
    if 2*n+1<=N:
        inord(2*n+1)

T = int(input())
for tc in range(1, T+1):
    cnt = 1
    N = int(input())
    tree = [0]*(N+1)
    inord(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
