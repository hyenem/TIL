T = int(input())
dxdy = ((0,0), (-1, 0), (0, 1), (1, 0), (0, -1))
for tc in range(1, T+1):
    ans = 0
    M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AP = [tuple(map(int, input().split())) for _ in range(K)]
    AP.sort(reverse=True, key = lambda x: x[3])
    ax, ay, bx, by = 1, 1, 10, 10
    for i in range(M+1):
        selected = [0, 0, 0]
        for y, x, c, p in AP:
            ad = abs(x-ax)+abs(y-ay)
            bd = abs(x-bx)+abs(y-by)
            if ad<=c and bd<=c:
                if sum(selected)!=0:
                    ans += p
                    break
                else :
                    ans += p
                    selected[2]=1
                    continue
            elif ad<=c:
                if selected[0]: continue
                elif selected[1]+selected[2]==1:
                    ans += p
                    break
                else :
                    ans+=p
                    selected[0]=1
                    continue
            elif bd<=c:
                if selected[1]: continue
                if selected[0]+selected[2]==1:
                    ans += p
                    break
                else :
                    ans += p
                    selected[1]=1
        if i==M: break
        ax, ay = ax+dxdy[A[i]][0], ay+dxdy[A[i]][1]
        bx, by = bx+dxdy[B[i]][0], by+dxdy[B[i]][1]

    print(f'#{tc} {ans}')