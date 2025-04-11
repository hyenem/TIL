T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr= [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            tmpans = arr[i][j]
            if tmpans*M>=1: ans = max(tmpans, ans)

            for k in range(1, 2*N+1):
                for x in range(-k, k+1):
                    for y in {k-abs(x), -k+abs(x)}:
                        if not (0<=x+i<N and 0<=j+y<N): continue
                        tmpans += arr[x+i][j+y]
                if k**2+(k+1)**2<=M*tmpans:
                    ans = max(ans, tmpans)

    print(f'#{tc} {ans}')